"use client"

import { useState } from 'react'
import { AlertCircle, FileDown, FileText, Loader2, Github } from 'lucide-react'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'

export default function HomePage() {
  const [markdown, setMarkdown] = useState('')
  const [status, setStatus] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const convertToPPT = async () => {
    if (!markdown.trim()) {
      setError('Please enter some markdown content')
      return
    }

    setLoading(true)
    setError('')
    setStatus('Converting...')

    try {
      const response = await fetch('/convert', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ markdown }),
      })

      if (response.ok) {
        const blob = await response.blob()
        const url = window.URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = 'presentation.pptx'
        document.body.appendChild(a)
        a.click()
        window.URL.revokeObjectURL(url)
        document.body.removeChild(a)
        setStatus('Conversion successful!')
      } else {
        throw new Error('Conversion failed')
      }
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

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header with Navigation */}
      <header className="bg-white shadow-sm">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo and Title */}
            <div className="flex items-center">
              <FileText className="h-8 w-8 text-blue-600" />
              <h1 className="ml-2 text-2xl font-bold text-gray-900">
                Markdown to PPT Converter
              </h1>
            </div>

            {/* Navigation Links */}
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
            <h2 className="text-lg font-semibold text-gray-900 mb-2">
              Quick Example
            </h2>
            <div className="bg-gray-50 rounded p-4">
              <pre className="text-sm text-gray-700 whitespace-pre-wrap">
{`# My Presentation

---

## Slide 1
- Point 1
- Point 2

---

## Slide 2
1. Numbered point
2. Another point`}
              </pre>
            </div>
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
              className="w-full h-64 p-4 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
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
            <li>Click "Convert to PowerPoint" to generate your presentation</li>
          </ol>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-8">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm">
            Made with ❤️ using Flask and React, By Hsu Po Hsiang
          </p>
        </div>
      </footer>
    </div>
  )
}