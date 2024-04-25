<template>
  <div
    class="flex items-center justify-center w-screen h-screen bg-gradient-to-r from-primary to-secondary"
  >
    <div class="px-40 py-20 bg-white rounded-md shadow-xl">
      <div class="flex flex-col items-center">
        <h1 class="font-bold text-blue-600 text-9xl">404</h1>

        <h6
          class="mb-2 text-2xl font-bold text-center text-gray-800 md:text-3xl"
        >
          <span class="text-red-500"></span> Page not found
        </h6>

        <p class="mb-8 text-center text-gray-500 md:text-lg">
          Die Seite, die Sie aufgerufen haben existiert nicht.
        </p>

        <router-link
          :to="{ name: 'Home' }"
          class="w-1/2 text-sm border border-transparent font-medium rounded-md text-white bg-primary hover:bg-primaryAccent md:py-4 md:px-10"
        >
          Zurück zum Start
        </router-link>
      </div>
    </div>
  </div>
</template>
