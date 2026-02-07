import React from 'react'
import { Link } from 'react-router-dom'

const FactCard = ({ fact, onDelete }) => {
  return (
    <div className="fact-card">
      <div className="flex justify-between items-start mb-3">
        <h3 className="text-lg font-semibold text-gray-900">{fact.title}</h3>
        <span className="category-badge">{fact.category}</span>
      </div>
      <p className="text-gray-700 mb-4 line-clamp-3">
        {fact.content}
      </p>
      <div className="flex justify-between items-center">
        <Link 
          to={`/fact/${fact.id}`}
          className="btn-secondary"
        >
          Read More
        </Link>
        {onDelete && (
          <button
            onClick={() => onDelete(fact.id)}
            className="btn-danger text-sm"
          >
            Delete
          </button>
        )}
      </div>
    </div>
  )
}

export default FactCard