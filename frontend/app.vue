

<!-- <template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtWelcome />
  </div>
</template> -->

<script setup lang="ts">
const config = useRuntimeConfig()
const { data } = await useFetch(`${config.public.apiBase}/`)
</script>

<template>
  <div v-if="data == null">
    No data
  </div>
  <div v-else>
    {{ data }}
  </div>
</template>
