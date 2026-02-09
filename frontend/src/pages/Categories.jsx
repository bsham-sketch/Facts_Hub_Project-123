import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'

const Categories = () => {
  const [categories, setCategories] = useState([])
  const [facts, setFacts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true)
        const [categoriesResponse, factsResponse] = await Promise.all([
          api.get('/api/categories/'),
          api.get('/api/facts/')
        ])
        
        setCategories(categoriesResponse.data.categories)
        setFacts(factsResponse.data.facts)
      } catch (err) {
        setError('Failed to load categories. Please try again later.')
        console.error('Error fetching categories:', err)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  const getFactCountByCategory = (category) => {
    return facts.filter(fact => fact.category === category).length
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
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Categories</h1>
        <p className="text-xl text-gray-600">
          Browse facts by category and explore topics that interest you.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {categories.map(category => (
          <Link
            key={category}
            to={`/facts/category/${category}`}
            className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition-shadow group"
          >
            <div className="text-center">
              <h3 className="text-2xl font-bold text-gray-900 mb-4 group-hover:text-blue-600 transition-colors">
                {category}
              </h3>
              <div className="w-16 h-16 bg-blue-100 rounded-full mx-auto mb-4 flex items-center justify-center">
                <span className="text-2xl">
                  {category === 'Science' && '🔬'}
                  {category === 'Industry' && '🏭'}
                  {category === 'Health' && '🏥'}
                  {category === 'Food' && '🍎'}
                  {category === 'Technology' && '💻'}
                  {category === 'Universe' && '🌌'}
                </span>
              </div>
              <p className="text-gray-600">
                {getFactCountByCategory(category)} fact{getFactCountByCategory(category) !== 1 ? 's' : ''}
              </p>
              <p className="text-sm text-gray-500 mt-2">Click to explore</p>
            </div>
          </Link>
        ))}
      </div>

      <div className="mt-12 text-center">
        <p className="text-gray-600 mb-4">Want to add a fact to a category?</p>
        <Link to="/add-fact" className="btn-primary">
          Add a New Fact
        </Link>
      </div>
    </div>
  )
}

export default Categories