<template>
  <section>
    <!-- component -->
    <div class="">
      <div id="ProgressStepper" class="flex">
        <!-- progress item -->
        <div class="w-1/3">
          <div class="relative mb-2">
            <div
              :class="{
                'bg-green-500 border-2 border-action': activestate == '1',
              }"
              class="w-10 h-10 mx-auto bg-gray-400 rounded-full text-lg text-white flex items-center"
            >
              <span class="text-center text-white font-bold w-full"> 1 </span>
            </div>
          </div>

          <h3
            class="text-xs invisible sm:visible sm:text-md md:text-lg lg:text-xl font-bold text-center"
          >
            Mitarbeiter*innen einladen
          </h3>
        </div>
        <!-- /progress item -->

        <!-- progress item middle -->
        <div class="w-1/3">
          <div class="relative mb-2">
            <div
              class="absolute flex align-center items-center align-middle content-center"
              style="
                width: calc(100% - 2.5rem - 1rem);
                top: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <div
                :class="[`bg-${linecolor}-200`]"
                class="w-full bg-white rounded items-center align-middle align-center flex-1"
              >
                <div
                  class="w-0 bg-green-300 py-1 rounded"
                  style="width: ${procentBar}%;"
                ></div>
                <!-- middle part 100 full & 50 half progressstatus-->
              </div>
            </div>

            <div
              :class="{ 'bg-action': activestate == '2' }"
              class="w-10 h-10 mx-auto bg-gray-400 rounded-full text-lg text-white flex items-center"
            >
              <span class="text-center text-white font-bold w-full"> 2 </span>
            </div>
          </div>

          <div
            class="text-xs invisible sm:visible sm:text-md md:text-lg lg:text-xl font-bold text-center"
          >
            ITS-Kompetztests durchführen
          </div>
        </div>
        <!-- progress item middle -->
        <div class="w-1/3">
          <div class="relative mb-2">
            <div
              class="absolute flex align-center items-center align-middle content-center"
              style="
                width: calc(100% - 2.5rem - 1rem);
                top: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <div
                :class="[`bg-${linecolor}-200`]"
                class="w-full bg-white rounded items-center align-middle align-center flex-1"
              >
                <div
                  class="w-0 bg-green-300 py-1 rounded"
                  style="width: ${procentBar}%;"
                ></div>
                <!-- middle part 100 full & 50 half progressstatus-->
              </div>
            </div>

            <div
              :class="{ 'bg-action': activestate == '3' }"
              class="w-10 h-10 mx-auto bg-gray-400 rounded-full text-lg text-white flex items-center"
            >
              <span class="text-center text-white font-bold w-full"> 3 </span>
            </div>
          </div>

          <div
            class="text-xs invisible sm:visible sm:text-md md:text-lg lg:text-xl font-bold text-center"
          >
            Management Report erhalten
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    linecolor: {
      type: String,
      default: "gray",
    },
    activestate: {
      type: Number,
      default: 0,
    },
  },
};
</script>
