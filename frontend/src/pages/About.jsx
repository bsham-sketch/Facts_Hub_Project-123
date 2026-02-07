import React from 'react'
import { Link } from 'react-router-dom'

const About = () => {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">About Facts Hub</h1>
        <p className="text-xl text-gray-600">
          A simple full-stack application for discovering and sharing interesting facts.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Mission</h2>
          <p className="text-gray-700 mb-4">
            Facts Hub was created to make learning fun and accessible. We believe that knowledge 
            should be shared freely and that everyone has something interesting to contribute.
          </p>
          <p className="text-gray-700">
            Our platform allows users to discover fascinating facts across various categories 
            and contribute their own knowledge to help others learn.
          </p>
        </div>

        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">What We Offer</h2>
          <ul className="space-y-3 text-gray-700">
            <li className="flex items-start">
              <span className="text-blue-600 mr-2">•</span>
              Browse facts by category (Science, Industry, Health, Food, Technology)
            </li>
            <li className="flex items-start">
              <span className="text-blue-600 mr-2">•</span>
              Read detailed explanations for each fact
            </li>
            <li className="flex items-start">
              <span className="text-blue-600 mr-2">•</span>
              Contribute your own interesting facts
            </li>
            <li className="flex items-start">
              <span className="text-blue-600 mr-2">•</span>
              Clean, responsive design that works on all devices
            </li>
          </ul>
        </div>
      </div>

      <div className="bg-white p-8 rounded-lg shadow-md mb-12">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Fact Categories</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="text-center p-4">
            <div className="w-12 h-12 bg-blue-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">🔬</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Science</h3>
            <p className="text-sm text-gray-600">
              Discover amazing scientific facts about the universe, biology, physics, and more
            </p>
          </div>

          <div className="text-center p-4">
            <div className="w-12 h-12 bg-green-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">🏭</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Industry</h3>
            <p className="text-sm text-gray-600">
              Learn about industrial innovations, manufacturing processes, and technological advancements
            </p>
          </div>

          <div className="text-center p-4">
            <div className="w-12 h-12 bg-purple-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">🏥</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Health</h3>
            <p className="text-sm text-gray-600">
              Explore facts about human health, medical discoveries, and wellness tips
            </p>
          </div>

          <div className="text-center p-4">
            <div className="w-12 h-12 bg-orange-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">🍎</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Food</h3>
            <p className="text-sm text-gray-600">
              Interesting facts about food origins, nutrition, cooking, and culinary traditions
            </p>
          </div>

          <div className="text-center p-4">
            <div className="w-12 h-12 bg-red-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">💻</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Technology</h3>
            <p className="text-sm text-gray-600">
              Fascinating facts about computers, software, gadgets, and digital innovations
            </p>
          </div>

          <div className="text-center p-4">
            <div className="w-12 h-12 bg-indigo-100 rounded-full mx-auto mb-4 flex items-center justify-center">
              <span className="text-2xl">🌌</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Universe</h3>
            <p className="text-sm text-gray-600">
              Explore mind-blowing facts about space, stars, galaxies, and the mysteries of the cosmos
            </p>
          </div>
        </div>
      </div>

      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Get Started</h2>
        <p className="text-gray-600 mb-8">
          Ready to explore some interesting facts? Start by browsing our categories or 
          add your own fact to share with the community!
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
    </div>
  )
}

export default About