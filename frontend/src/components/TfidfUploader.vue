<template>
  <div class="p-6 max-w-3xl mx-auto">
    <h1 class="text-xl font-bold mb-4">Загрузка файла и просмотр TF-IDF</h1>

    <input type="file" @change="uploadFile" class="mb-4"/>

    <div v-if="documentId" class="mt-4">
      <h2 class="text-lg font-semibold">Результаты (топ-50 слов):</h2>
      <table v-if="statistics.length" class="table-auto w-full border-collapse border border-gray-300 mt-2">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 p-2">№</th>
            <th class="border border-gray-300 p-2">Слово</th>
            <th class="border border-gray-300 p-2">TF</th>
            <th class="border border-gray-300 p-2">IDF</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in statistics" :key="item.слово">
            <td class="border border-gray-300 p-2 text-center">{{ index + 1 }}</td>
            <td class="border border-gray-300 p-2">{{ item.слово }}</td>
            <td class="border border-gray-300 p-2 text-center">{{ item.tf }}</td>
            <td class="border border-gray-300 p-2 text-center">{{ item.idf.toFixed(3) }}</td>
          </tr>
        </tbody>
      </table>

      <div v-else class="mt-2 text-gray-500">Идет обработка данных...</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const documentId = ref(null)
const statistics = ref([])
const baseUrl = 'http://localhost:8000'

const uploadFile = async (event) => {
  const file = event.target.files[0]
  if (!file) return
  const formData = new FormData()
  formData.append('file', file)

  const uploadResponse = await axios.post(`${baseUrl}/document/`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

  documentId.value = uploadResponse.data.id
  pollResults()
}

// Polling для обновления данных каждые 2 сек.
const pollResults = async () => {
  const interval = setInterval(async () => {
    const response = await axios.get(`${baseUrl}/document/${documentId.value}/`)
    if (response.data.statistics) {
      statistics.value = response.data.statistics
      clearInterval(interval)
    }
  }, 2000)
}
</script>

<style>
body {
  font-family: 'Inter', sans-serif;
}
</style>