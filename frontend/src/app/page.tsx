"use client"

import { useState } from 'react'
import { 
  AlertCircle, 
  FileDown, 
  FileText, 
  Loader2, 
  Github, 
  ChevronDown, 
  ChevronUp, 
  Copy 
} from 'lucide-react'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import MarkdownToPptConverter from '@/lib/converter'

const exampleMarkdown = `# Artificial Intelligence: An Overview

---

## Introduction

- Definition of AI
- Brief history of AI
- Importance of AI in the modern world

---

## Table of Contents

1. Core Features
2. Use Cases
3. Advantages
4. Limitations
5. Future Directions

---

## Core Features

- **Machine Learning**: Algorithms improve automatically through experience.
- **Natural Language Processing (NLP)**: Interaction between computers and humans using natural language.
- **Robotics**: Machines performing tasks with high precision and autonomy.
- **Computer Vision**: Enables machines to interpret and process visual data from the world.

---

## Use Cases

- **Healthcare**: Predictive analytics for patient care and disease diagnosis.
- **Finance**: Fraud detection and automated trading systems.
- **Manufacturing**: Predictive maintenance and optimized production lines.
- **Education**: Personalized learning experiences and automation of administrative tasks.

---

## Advantages

- **Efficiency and Speed**: Performing complex computations and data analyses rapidly.
- **Accuracy**: High precision in tasks like medical diagnoses and data entry.
- **Automation of Mundane Tasks**: Freeing up humans for creative and strategic roles.
- **Data Handling Capabilities**: Processing and interpreting vast amounts of data efficiently.

---

## Limitations

- **Ethical and Privacy Concerns**: Issues around data misuse and bias in AI algorithms.
- **High Costs**: Initial setup and maintenance of AI systems can be expensive.
- **Dependency and Job Displacement**: Potential for increased dependency on technology and displacement of jobs.
- **Complexity**: Designing, implementing, and maintaining AI systems require specialized knowledge.

---

## Future Directions

- **Ethical AI**: Developing guidelines and frameworks for the responsible use of AI.
- **Explainable AI**: Making AI decisions more transparent and understandable.
- **Integration into Everyday Life**: More seamless integration of AI in daily activities and industries.
- **Advancements in AI Technology**: Ongoing research to enhance AI's capabilities and reduce limitations.

---

`;

export default function HomePage() {
  const [markdown, setMarkdown] = useState('')
  const [status, setStatus] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [isExampleOpen, setIsExampleOpen] = useState(false)

  const convertToPPT = async () => {
    if (!markdown.trim()) {
      setError('Please enter some markdown content')
      return
    }

    setLoading(true)
    setError('')
    setStatus('Converting...')

    try {
      const converter = new MarkdownToPptConverter(markdown)
      const pptxContent = await converter.convert()
      
      const blob = new Blob([pptxContent], { 
        type: 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
      })
      
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = 'presentation.pptx'
      a.style.display = 'none'
      document.body.appendChild(a)
      
      setTimeout(() => {
        document.body.removeChild(a)
        URL.revokeObjectURL(url)
      }, 100)
      
      setStatus('Conversion successful!')
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message)
      } else {
        setError('An unknown error occurred')
      }
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  const applyExample = () => {
    setMarkdown(exampleMarkdown)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header with Navigation */}
      <header className="bg-white shadow-sm">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <FileText className="h-8 w-8 text-blue-600" />
              <h1 className="ml-2 text-2xl font-bold text-gray-900">
                Markdown to PPT Converter
              </h1>
            </div>

            <div className="flex items-center space-x-4">
              <a
                href="https://github.com/treeleaves30760/Markdown_PPT_Converter"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-3 py-2 text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors"
              >
                <Github className="h-5 w-5 mr-1" />
                GitHub
              </a>
              <a
                href="https://chatgpt.com/g/g-YiXZ7cBcg-ppt-creator"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-3 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                Try GPTs Generation
              </a>
            </div>
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow p-6">
          {/* Example Section */}
          <div className="mb-6">
            <button
              onClick={() => setIsExampleOpen(!isExampleOpen)}
              className="w-full flex items-center justify-between text-lg font-semibold text-gray-900 mb-2 hover:text-blue-600 transition-colors"
            >
              <span>Quick Example</span>
              {isExampleOpen ? (
                <ChevronUp className="h-5 w-5" />
              ) : (
                <ChevronDown className="h-5 w-5" />
              )}
            </button>
            {isExampleOpen && (
              <div className="bg-gray-50 rounded-lg p-4">
                <div className="flex justify-end mb-2">
                  <button
                    onClick={applyExample}
                    className="inline-flex items-center px-3 py-1.5 text-sm font-medium text-gray-700 hover:text-blue-600 transition-colors border border-gray-300 rounded-md hover:border-blue-600"
                  >
                    <Copy className="h-4 w-4 mr-1" />
                    Use This Example
                  </button>
                </div>
                <pre className="text-sm text-gray-700 whitespace-pre-wrap">
                  {exampleMarkdown}
                </pre>
              </div>
            )}
          </div>

          {/* Editor Section */}
          <div className="mb-6">
            <label
              htmlFor="markdown"
              className="block text-sm font-medium text-gray-700 mb-2"
            >
              Your Markdown
            </label>
            <textarea
              id="markdown"
              className="w-full h-[43vh] p-4 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Enter your markdown here..."
              value={markdown}
              onChange={(e) => setMarkdown(e.target.value)}
            />
          </div>

          {/* Action Button */}
          <div className="flex justify-end">
            <button
              onClick={convertToPPT}
              disabled={loading}
              className="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? (
                <Loader2 className="animate-spin -ml-1 mr-2 h-5 w-5" />
              ) : (
                <FileDown className="-ml-1 mr-2 h-5 w-5" />
              )}
              {loading ? 'Converting...' : 'Convert to PowerPoint'}
            </button>
          </div>

          {/* Status Messages */}
          {status && (
            <div className="mt-4">
              <Alert>
                <AlertTitle>Success</AlertTitle>
                <AlertDescription>{status}</AlertDescription>
              </Alert>
            </div>
          )}

          {error && (
            <div className="mt-4">
              <Alert variant="destructive">
                <AlertCircle className="h-4 w-4" />
                <AlertTitle>Error</AlertTitle>
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            </div>
          )}
        </div>

        {/* Instructions */}
        <div className="mt-8 bg-white rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">
            How to Use
          </h2>
          <ol className="list-decimal list-inside space-y-2 text-gray-700">
            <li>Enter your markdown content in the text area above</li>
            <li>Use --- to separate slides</li>
            <li>Use # for title and ## for slide headers</li>
            <li>Use - for bullet points and 1. for numbered lists</li>
            <li>Use **text** for bold text</li>
            <li>Click &quot;Convert to PowerPoint&quot; to generate your presentation</li>
          </ol>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-8">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm">
            Made with ❤️ using Next.js and PptxGenJS, By Hsu Po Hsiang
          </p>
        </div>
      </footer>
    </div>
  )
}