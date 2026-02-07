import React, { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import api from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'

const FactDetails = () => {
  const { id } = useParams()
  const [fact, setFact] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchFact = async () => {
      try {
        setLoading(true)
        setError(null)
        
        const response = await api.get(`/facts/${id}/`)
        setFact(response.data.fact)
      } catch (err) {
        if (err.response?.status === 404) {
          setError('Fact not found.')
        } else {
          setError('Failed to load fact. Please try again later.')
        }
        console.error('Error fetching fact:', err)
      } finally {
        setLoading(false)
      }
    }

    fetchFact()
  }, [id])

  const handleDeleteFact = async () => {
    if (!window.confirm('Are you sure you want to delete this fact?')) {
      return
    }

    try {
      await api.delete(`/facts/${id}/`)
      // Redirect to home or categories page after deletion
      window.location.href = '/'
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
        <p className="text-red-600 text-lg mb-4">{error}</p>
        <div className="space-x-4">
          <Link to="/" className="btn-primary">
            Back to Home
          </Link>
          <button 
            onClick={() => window.location.reload()}
            className="btn-secondary"
          >
            Try Again
          </button>
        </div>
      </div>
    )
  }

  if (!fact) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 text-lg mb-4">Fact not found.</p>
        <Link to="/" className="btn-primary">
          Back to Home
        </Link>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <Link to="/" className="text-blue-600 hover:text-blue-800">
          ← Back to Home
        </Link>
      </div>

      <div className="fact-card">
        <div className="flex justify-between items-start mb-4">
          <div>
            <span className="category-badge">{fact.category}</span>
            <h1 className="text-3xl font-bold text-gray-900 mt-2">{fact.title}</h1>
          </div>
          <div className="flex space-x-2">
            <Link 
              to="/add-fact" 
              className="btn-secondary text-sm"
            >
              Edit
            </Link>
            <button 
              onClick={handleDeleteFact}
              className="btn-danger text-sm"
            >
              Delete
            </button>
          </div>
        </div>
        
        <div className="prose max-w-none">
          <p className="text-gray-700 text-lg leading-relaxed whitespace-pre-wrap">
            {fact.content}
          </p>
        </div>
        
        <div className="mt-6 text-sm text-gray-500">
          Added on: {new Date(fact.created_at).toLocaleDateString()}
        </div>
      </div>

      <div className="mt-8 text-center">
        <Link to="/categories" className="btn-secondary">
          Browse More Categories
        </Link>
      </div>
    </div>
  )
}

export default FactDetails