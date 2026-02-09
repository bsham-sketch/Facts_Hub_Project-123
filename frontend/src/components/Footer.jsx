import React from 'react'

const Footer = () => {
  return (
    <footer className="bg-gray-50 border-t mt-12">
      <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Facts Hub</h3>
            <p className="text-gray-600">
              Discover interesting facts across various categories. Learn something new every day!
            </p>
          </div>
          
          <div>
            <h4 className="text-md font-semibold text-gray-900 mb-4">Categories</h4>
            <ul className="space-y-2 text-gray-600">
              <li>Science</li>
              <li>Industry</li>
              <li>Health</li>
              <li>Food</li>
              <li>Technology</li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-md font-semibold text-gray-900 mb-4">Connect</h4>
            <p className="text-gray-600">
              Built with React, Django, and Tailwind CSS. A simple full-stack application for fact management.
            </p>
          </div>
        </div>
        
        <div className="border-t border-gray-200 mt-8 pt-8 text-center text-gray-500">
          <p>&copy; 2026 Facts Hub. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer