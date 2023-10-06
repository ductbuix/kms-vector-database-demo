'use client'

import { useState, ChangeEvent } from 'react'

interface UploaderProps {
  onUpload: (data: FormData) => void
}

export default function Uploader({ onUpload }: UploaderProps) {
  const [image, setImage] = useState<File | undefined>(undefined)

  const onImageCHange = (event: ChangeEvent<HTMLInputElement>) => {
    const { files } = event.currentTarget
    console.log(files?.[0])

    if (files?.[0]) {
      setImage(files?.[0])
    }
  }

  const onSubmit = (event: ChangeEvent<HTMLFormElement>) => {
    event.preventDefault()

    if (image) {
      const formData = new FormData()
      formData.append('image', image)

      console.log('Form Data', formData)
      onUpload(formData)
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <form onSubmit={onSubmit}>
        <label htmlFor="upload">Upload your image</label>
        <input id="upload" type="file" onChange={onImageCHange} />
        <button type="submit">Submit</button>
      </form>
    </main>
  )
}
