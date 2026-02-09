import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'
import FactCard from '../components/FactCard'

const Home = () => {
  const [facts, setFacts] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchFacts = async () => {
      try {
        const res = await api.get("/api/facts/");
        setFacts(res.data.facts);
      } catch (err) {
        console.error(err);
        setError(true);
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

  return (
    <div className="max-w-7xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome to Facts Hub
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Discover interesting facts across various categories and learn something new every day!
        </p>
        <div className="flex justify-center space-x-4">
          <Link to="/categories" className="btn-primary">
            Browse Categories
          </Link>
          <Link to="/add-fact" className="btn-secondary">
            Add a Fact
          </Link>
        </div>
      </div>

      <div className="mb-12">
        <h2 className="text-2xl font-semibold text-gray-900 mb-6">Featured Facts</h2>
        {facts.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {facts.slice(0, 6).map(fact => (
              <FactCard 
                key={fact.id} 
                fact={fact} 
                onDelete={handleDeleteFact}
              />
            ))}
          </div>
        ) : (
          <div className="text-center py-8">
            <p className="text-gray-500">No facts available yet. Be the first to add one!</p>
          </div>
        )}
      </div>

      <div>
        <h2 className="text-2xl font-semibold text-gray-900 mb-6">Explore Categories</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {categories.map(category => (
            <Link
              key={category}
              to={`/facts/category/${category}`}
              className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow text-center"
            >
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{category}</h3>
              <p className="text-sm text-gray-600">
                {facts.filter(fact => fact.category === category).length} facts
              </p>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}

export default Home