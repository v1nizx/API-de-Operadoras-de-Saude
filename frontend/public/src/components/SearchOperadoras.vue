<template>
  <div>
    <input v-model="searchTerm" @input="fetchOperadoras" placeholder="Buscar operadoras...">
    <button @click="fetchOperadoras">Buscar</button>
    
    <div v-if="loading">Carregando...</div>
    
    <table v-if="results.length">
      <tr v-for="op in results" :key="op.id">
        <td>{{ op['Razão Social'] }}</td>
        <td>{{ op.CNPJ }}</td>
      </tr>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const searchTerm = ref('')
const results = ref([])
const loading = ref(false)

const fetchOperadoras = async () => {
  loading.value = true
  try {
    const response = await axios.get('http://localhost:8000/operadoras/')
    results.value = response.data
    console.log('Dados recebidos:', results.value) // Verifique no console
  } catch (error) {
    console.error('Erro na requisição:', error)
  } finally {
    loading.value = false
  }
}

// Busca inicial ao carregar o componente
fetchOperadoras()
</script>