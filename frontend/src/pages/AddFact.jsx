import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api, { endpoints } from '../services/api'
import FactForm from '../components/FactForm'

const AddFact = () => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const handleSubmit = async (factData) => {
    if (!factData) {
      navigate('/add-fact')
      return
    }

    try {
      setLoading(true)
      setError(null)
      
      const response = await api.post(endpoints.factAdd, factData)
      
      // Redirect to the newly created fact's detail page
      navigate(`/fact/${response.data.fact.id}`)
    } catch (err) {
      setError('Failed to add fact. Please try again.')
      console.error('Error adding fact:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto">
      <div className="mb-8">
        <button 
          onClick={() => navigate(-1)}
          className="text-blue-600 hover:text-blue-800"
        >
          ← Back
        </button>
      </div>

      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Add New Fact</h1>
        <p className="text-gray-600">
          Share an interesting fact with the world!
        </p>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-6">
          {error}
        </div>
      )}

      <div className="bg-white rounded-lg shadow-md p-8">
        <FactForm 
          onSubmit={handleSubmit}
          isLoading={loading}
        />
      </div>

      <div className="mt-8 text-center">
        <p className="text-gray-500 text-sm">
          Your fact will be reviewed and added to the appropriate category.
        </p>
      </div>
    </div>
  )
}

export default AddFact