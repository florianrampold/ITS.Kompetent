<template>
  <div
    class="grid grid-cols-1 lg:grid-cols-2 bg-white gap-10 rounded-lg shadow-lg py-10 px-10"
  >
    <div class="flex flex-col">
      <h1
        class="text-2xl tracking-tight font-extrabold text-primary text-left sm:text-3xl md:text-64xl pb-6"
      >
        <slot name="heading"></slot>
      </h1>
      <div class="border-b-4 w-14 border-primary"></div>

      <p
        class="mt-3 text-base text-gray-500 text-left font-semibold sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        <slot name="title"></slot>
      </p>
      <p
        class="mt-3 text-sm text-left text-primary font-medium sm:mt-5 sm:text-base md:max-w-2xl md:mx-auto md:mt-5 md:text-lg lg:mx-0"
      >
        <slot name="content"></slot>
      </p>
    </div>

    <div class="flex flex-col justify-center items-center">
      <slot name="image"></slot>
    </div>
  </div>
</template>
