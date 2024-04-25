<template>
  <div
    class="xl:relative bg-white rounded-lg shadow-lg border border-gray-200 xl:h-256"
  >
    <div class="flex justify-center pt-12 items-center">
      <slot name="icon"></slot>
    </div>

    <div class="xl:absolute lg:top-64 p-5">
      <slot name="button"></slot>
      <p
        class="pt-8 text-base text-primary font-semibold sm:mt-5 sm:text-lg sm:max-w-xl px-5 md:mt-5 md:text-xl i lg:mx-0"
      >
        <slot name="title"></slot>
      </p>
      <p
        class="mt-3 text-sm text-left text-gray-500 font-medium sm:mt-5 sm:text-base md:max-w-2xl md:mx-auto md:mt-5 md:text-lg lg:mx-0"
      >
        <slot name="content"></slot>
      </p>
    </div>
  </div>
</template>
