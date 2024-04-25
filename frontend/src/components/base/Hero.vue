<template>
  <main class="bg-white pb-20">
    <div class="standard-container">
      <div class="mb-20">
        <slot name="centered-item" />
      </div>

      <div class="grid grid-cols-1 gap-10 lg:grid-cols-5">
        <div class="col-span-5 md:col-span-3 text-center lg:text-left">
          <slot name="title" />
          <slot name="content" />
          <slot name="buttons" />
        </div>
        <div class="ml-10 col-span-5 md:col-span-2">
          <slot name="image" />
        </div>
      </div>

      <div class="w-full mt-20">
        <slot name="progress" />
      </div>
    </div>
  </main>
</template>

<style scoped>
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
</style>
