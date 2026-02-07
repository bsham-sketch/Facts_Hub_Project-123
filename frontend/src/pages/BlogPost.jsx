import React, { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'

const BlogPost = () => {
  const { id } = useParams()
  const [post, setPost] = useState(null)
  const [loading, setLoading] = useState(true)

  // Mock blog posts data (in a real app, this would come from an API)
  const blogPosts = [
    {
      id: 1,
      title: "The Science Behind Everyday Phenomena",
      content: `
        <p>Have you ever wondered why the sky is blue? Or why ice floats on water? These are just a few of the fascinating scientific phenomena that occur around us every day.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The Blue Sky Mystery</h3>
        <p>The sky appears blue due to a phenomenon called Rayleigh scattering. When sunlight enters Earth's atmosphere, it collides with gas molecules. Blue light has a shorter wavelength and gets scattered more than other colors, making the sky appear blue to our eyes.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">Ice That Defies Gravity</h3>
        <p>Unlike most substances, water expands when it freezes. This unique property means that ice is less dense than liquid water, which is why ice cubes float in your drink. This phenomenon is crucial for aquatic life, as it allows ice to form on the surface of lakes and rivers, insulating the water below.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The Science of Bubbles</h3>
        <p>Bubbles are fascinating examples of surface tension at work. The soap film that forms a bubble is made up of three layers: a thin layer of water sandwiched between two layers of soap molecules. This structure allows bubbles to maintain their spherical shape and creates the beautiful rainbow colors we see on their surface.</p>
      `,
      date: "January 15, 2024",
      category: "Science",
      readTime: "5 minutes"
    },
    {
      id: 2,
      title: "How Technology is Shaping Our Future",
      content: `
        <p>Technology is advancing at an unprecedented pace, transforming every aspect of our lives. From artificial intelligence to quantum computing, the future is being written in code.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The AI Revolution</h3>
        <p>Artificial intelligence is no longer science fiction. AI systems can now compose music, write articles, and even diagnose medical conditions with remarkable accuracy. As AI continues to evolve, it will revolutionize industries from healthcare to transportation.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">Quantum Computing</h3>
        <p>Quantum computers operate on principles that defy classical physics. Using quantum bits or "qubits," these machines can process information in ways that traditional computers cannot, potentially solving complex problems in seconds that would take current supercomputers thousands of years.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The Internet of Things</h3>
        <p>The Internet of Things (IoT) is connecting our world in unprecedented ways. Smart homes, wearable devices, and connected cities are just the beginning. As more devices become interconnected, we're creating a seamless web of information that will transform how we live and work.</p>
      `,
      date: "January 10, 2024",
      category: "Technology",
      readTime: "7 minutes"
    },
    {
      id: 3,
      title: "The Health Benefits of Common Foods",
      content: `
        <p>The foods we eat every day contain powerful compounds that can boost our health and prevent disease. Let's explore the science behind some common superfoods.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The Mighty Avocado</h3>
        <p>Avocados are packed with heart-healthy monounsaturated fats, fiber, and over 20 different vitamins and minerals. They're particularly rich in potassium, which helps regulate blood pressure, and lutein, which supports eye health.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">Broccoli: Nature's Pharmacy</h3>
        <p>Broccoli contains sulforaphane, a compound that has been shown to have anti-cancer properties. It's also an excellent source of vitamin C, vitamin K, and folate. Regular consumption of broccoli has been linked to reduced risk of heart disease and improved digestion.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">The Power of Berries</h3>
        <p>Berries are loaded with antioxidants, particularly anthocyanins, which give them their vibrant colors. These compounds help protect our cells from damage and have been linked to improved brain function, reduced inflammation, and better heart health.</p>
        
        <h3 class="text-xl font-semibold mt-6 mb-4">Dark Chocolate Delight</h3>
        <p>Yes, chocolate can be good for you! Dark chocolate with at least 70% cocoa content is rich in flavonoids, which have been shown to improve blood flow, lower blood pressure, and reduce the risk of heart disease. Just remember to enjoy it in moderation.</p>
      `,
      date: "January 5, 2024",
      category: "Health",
      readTime: "4 minutes"
    }
  ]

  useEffect(() => {
    const fetchPost = () => {
      setLoading(true)
      // Find the blog post by ID
      const foundPost = blogPosts.find(post => post.id === parseInt(id))
      setPost(foundPost)
      setLoading(false)
    }

    fetchPost()
  }, [id])

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto py-12">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded mb-4"></div>
          <div className="h-4 bg-gray-200 rounded mb-2"></div>
          <div className="h-4 bg-gray-200 rounded mb-6"></div>
          <div className="space-y-4">
            <div className="h-4 bg-gray-200 rounded"></div>
            <div className="h-4 bg-gray-200 rounded"></div>
            <div className="h-4 bg-gray-200 rounded w-3/4"></div>
          </div>
        </div>
      </div>
    )
  }

  if (!post) {
    return (
      <div className="text-center py-12">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Blog Post Not Found</h2>
        <p className="text-gray-600 mb-8">The blog post you're looking for doesn't exist.</p>
        <Link to="/blog" className="btn-primary">
          Back to Blog
        </Link>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <Link 
          to="/blog" 
          className="text-blue-600 hover:text-blue-800 mb-4 inline-block"
        >
          ← Back to Blog
        </Link>
      </div>

      <article className="bg-white rounded-lg shadow-md p-8">
        <div className="flex justify-between items-start mb-4">
          <div>
            <span className="category-badge">{post.category}</span>
            <h1 className="text-4xl font-bold text-gray-900 mt-2 mb-4">{post.title}</h1>
            <div className="flex space-x-4 text-gray-600">
              <span>{post.date}</span>
              <span>•</span>
              <span>{post.readTime} read</span>
            </div>
          </div>
        </div>

        <div 
          className="prose prose-lg max-w-none"
          dangerouslySetInnerHTML={{ __html: post.content }}
        />
      </article>

      <div className="mt-8 text-center">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Explore More</h2>
        <div className="space-x-4">
          <Link to="/blog" className="btn-primary">
            All Blog Posts
          </Link>
          <Link to="/categories" className="btn-secondary">
            Explore Facts
          </Link>
        </div>
      </div>
    </div>
  )
}

export default BlogPost