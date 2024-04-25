<template>
  <div
    class="flex flex-col items-center justify-center bg-white rounded-lg shadow-lg py-10 px-5"
  >
    <slot name="icon"></slot>
    <slot name="button"></slot>

    <p
      class="mt-3 text-base text-primary font-semibold sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
    >
      <slot name="title"></slot>
    </p>
    <p
      class="mt-3 text-sm text-justify text-primary font-medium sm:mt-5 sm:text-base md:max-w-2xl md:mx-auto md:mt-5 md:text-lg lg:mx-0"
    >
      <slot name="content"></slot>
    </p>
  </div>
</template>
