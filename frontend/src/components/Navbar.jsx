import React from 'react'
import { Link, useLocation } from 'react-router-dom'

const Navbar = () => {
  const location = useLocation()

  const isActive = (path) => {
    return location.pathname === path ? 'text-blue-600 font-semibold' : 'text-gray-600 hover:text-blue-600'
  }

  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">FH</span>
              </div>
              <span className="text-xl font-bold text-gray-800">Facts Hub</span>
            </Link>
          </div>
          
          <div className="flex space-x-8">
            <Link to="/" className={`inline-flex items-center px-1 pt-1 ${isActive('/')}`}>
              Home
            </Link>
            <Link to="/categories" className={`inline-flex items-center px-1 pt-1 ${isActive('/categories')}`}>
              Categories
            </Link>
            <Link to="/add-fact" className={`inline-flex items-center px-1 pt-1 ${isActive('/add-fact')}`}>
              Add Fact
            </Link>
            <Link to="/about" className={`inline-flex items-center px-1 pt-1 ${isActive('/about')}`}>
              About
            </Link>
            <Link to="/blog" className={`inline-flex items-center px-1 pt-1 ${isActive('/blog')}`}>
              Blog
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar