import React, { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import api from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'
import FactCard from '../components/FactCard'

const FactsList = () => {
  const { category } = useParams()
  const [facts, setFacts] = useState([])
  const [allFacts, setAllFacts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchFacts = async () => {
      try {
        const response = await api.get("/api/facts/");
        setFacts(response.data);
      } catch (error) {
        console.error("API ERROR:", error);
      }
    };

    fetchFacts();
  }, []);

  const handleDeleteFact = async (factId) => {
    if (!window.confirm('Are you sure you want to delete this fact?')) {
      return
    }

    try {
      await api.delete(`/facts/${factId}/`)
      setFacts(prevFacts => prevFacts.filter(fact => fact.id !== factId))
      setAllFacts(prevFacts => prevFacts.filter(fact => fact.id !== factId))
    } catch (err) {
      alert('Failed to delete fact. Please try again.')
      console.error('Error deleting fact:', err)
    }
  }

  if (loading) {
    return <LoadingSpinner />
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600">{error}</p>
        <button 
          onClick={() => window.location.reload()}
          className="btn-primary mt-4"
        >
          Try Again
        </button>
      </div>
    )
  }

  const displayCategory = category || 'All'

  return (
    <div className="max-w-7xl mx-auto">
      <div className="mb-8">
        <Link to="/" className="text-blue-600 hover:text-blue-800">
          ← Back to Home
        </Link>
      </div>

      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          {displayCategory} Facts
        </h1>
        <p className="text-xl text-gray-600">
          {facts.length} fact{facts.length !== 1 ? 's' : ''} found
        </p>
      </div>

      {facts.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {facts.map(fact => (
            <FactCard 
              key={fact.id} 
              fact={fact} 
              onDelete={handleDeleteFact}
            />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-500 text-lg mb-6">
            No facts found in the {displayCategory} category.
          </p>
          <div className="space-x-4">
            <Link to="/add-fact" className="btn-primary">
              Add a Fact
            </Link>
            <Link to="/categories" className="btn-secondary">
              Browse Categories
            </Link>
          </div>
        </div>
      )}
    </div>
  )
}

export default FactsList