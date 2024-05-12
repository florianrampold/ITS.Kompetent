<template>
  <Hero
    ><template #title>
      <h1 class="main-heading">
        <span class="text-primary xl:inline">ITS.Kompetent <br /> </span>
        {{ " " }}
        <span class="text-secondary xl:inline">Das Projekt</span>
      </h1></template
    >
    <template #content>
      <p
        class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        Das Verbundprojekt "ITS.Kompetent: Ermittlung des
        IT-Sicherheits-Qualifizierungsbedarfs mittels Kompetenzmessung und
        Profilabgleich" hat die Entwicklung des Online-Tools "ITS.Kompetent" zum
        Ziel.
      </p></template
    >
    <template #buttons>
      <div
        class="mt-5 w-full sm:mt-8 flex flex-col sm:flex-row justify-center gap-y-4 sm:gap-4 items-center lg:justify-start"
      >
        <div class="sm:w-2/5 md:w-2/5 w-3/5 2xl:w-2/6">
          <a
            href="https://www.uni-goettingen.de/de/its.kompetent+%28bmwi%29%2c+2021-2024/647031.html"
            target="__blank"
            class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent md:py-4 md:text-lg md:px-10"
          >
            Mehr erfahren
          </a>
        </div>
      </div></template
    >
  
  </Hero>
  <div class="page-background">
    <h1
      class="text-4xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-5xl md:text-6xl md:py-10"
    >
      Partner
    </h1>

    <div
      class="standard-container grid grid-cols-1 md:grid-cols-2 2xl:grid-cols-3 gap-10 mt-10 md:mt-0"
    >
      <Card>
        <template #icon
          ><img
            class="h-40"
            :src="require('@/assets/isc.png')"
            alt="ISC_logo"
          />
        </template>
        <template #button>
          <a
            class="btn-primary mt-4"
            href="https://www.uni-goettingen.de/de/306829.html"
            target="_blank"
            >Mehr erfahren</a
          >
        </template>
        <template #title>
          Juniorprofessur für Informationssicherheit und Compliance
        </template>
        <template #content
          >Die Professur für Informationssicerheit und Compliance ist an der
          Georg-August-Universität angesiedelt. Das Team betreibt
          anwendungsorientierte Forschung, die in führenden wissenschaftlichen
          Zeitschriften in den Bereichen sicheres und zuverlässiges Design von
          Informationssystemen, Netzwerk-Governance von Plattform-Ökosystemen
          und IT-Akzeptanzforschung publiziert wird. Alle Mitarbeiter:innen
          verfügen über fundierte Kenntnisse im Systemdesign mit
          Zertifizierungen wie ISO27001, TOGAF, CISSP oder ITIL.</template
        >
      </Card>
      <Card>
        <template #icon
          ><img class="h-40" :src="require('@/assets/im.png')" alt="IM_logo" />
        </template>
        <template #title> Professur für Informationsmanagement </template>
        <template #content
          >Der Lehrstuhl für Informationsmanagement unter der Leitung von
          Professor Dr. Lutz M. Kolbe, sieht das Management von Informationen
          und Informationstechnologien als Schlüssel für einen nachhaltigen
          Unternehmenserfolg. Dabei kooperiert der Lehrstuhl mit verschiedenen
          Partnern aus Wirtschaft und Forschung, vor allem in
          drittmittelfinanzierten Forschungsprojekten. Die aktuellen
          Forschungsthemen des Lehrstuhls fokussieren sich auf ganzheitliche
          Perspektiven für ein nachhaltiges Informationsmanagement (IM). Die
          Aktivitäten des Lehrstuhls gliedern sich in die Bereiche Mobility,
          Healthcare und Digital Transformation.</template
        ><template #button>
          <a
            class="btn-primary mt-4"
            href="https://www.uni-goettingen.de/de/57609.html"
            target="_blank"
            >Mehr erfahren</a
          >
        </template>
      </Card>
      <Card>
        <template #icon
          ><img
            class="h-16 lg:h-24"
            :src="require('@/assets/hohenheim.svg')"
            alt="Hohenheim_logo"
          />
        </template>
        <template #title> Professur für Wirtschaftspädagogik </template>
        <template #content
          >Der Lehrstuhl für Wirtschaftspädagogik ist an der Universität
          Hohenheim angesiedelt. Das Team forscht und lehrt zu verschiedenen
          Themen der beruflichen Bildung und publiziert wissenschaftliche
          Erkenntnisse in renommierten internationalen Fachzeitschriften. Ein
          zentraler Fokus liegt auf Merkmalen der Lehrprofessionalität und
          Fragen der Kompetenzmodellierung, -messung und -förderung in
          Ausbildung und Beruf, wobei heuristische Modelle sowie quantitative
          und qualitative Forschungsmethoden zum Einsatz kommen.</template
        ><template #button>
          <a
            class="btn-primary mt-4"
            href="https://wipaed.uni-hohenheim.de/"
            target="_blank"
            >Mehr erfahren</a
          >
        </template>
      </Card>
    </div>
  </div>
  <div class="py-10 mb-20">
    <h1
      class="text-3xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-4xl md:text-5xl py-10"
    >
      Assoziierte Partner
    </h1>
    <div
      class="standard-container grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 px-6 lg:px-20"
    >
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/watttron.jpg')"
        alt="watttron_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/snic.jpg')"
        alt="snic_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/sns.jpg')"
        alt="sns_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/dkub.jpg')"
        alt="dkub_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/oes.jpg')"
        alt="oes_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/abs.jpg')"
        alt="abs_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/fhr.jpg')"
        alt="fhr_logo"
      />
      <img
        class="md:p-5 lg:p-10"
        :src="require('@/assets/logos/rpd.jpg')"
        alt="rpd_logo"
      />
    </div>
  </div>
  <div class="page-background">
    <h1
      class="text-3xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-4xl md:text-5xl md:pt-10"
    >
      Partner der Initiative
    </h1>
    <div
      class="standard-container grid grid-cols-1 md:grid-cols-3 items-center mt-5 md:mt-0"
    >
      <a
        href="https://www.mittelstand-digital.de/MD/Navigation/DE/Home/home.html"
        class="p-10 sm:p-16 lg:p-20"
        target="_blank"
      >
        <img
          :src="require('@/assets/logos/mittelstand-digital.png')"
          alt="mittelstand-digital_logo"
        />
      </a>
      <a
        href="https://www.it-sicherheit-in-der-wirtschaft.de/ITS/Navigation/DE/Home/home.html"
        class="p-10 sm:p-16 lg:p-20"
        target="_blank"
        ><img
          :src="require('@/assets/logos/it-sicherheit-idw.png')"
          alt="it-sicherheit-idw_logo"
      /></a>
      <a
        href="https://www.bmwi.de/Navigation/DE/Home/home.html"
        class="p-10 sm:p-16 lg:p-20"
        target="_blank"
        ><img :src="require('@/assets/logos/BMWi.png')" alt="BMWi_logo"
      /></a>
    </div>
  </div>
</template>
<script>
import Hero from "@/components/base/Hero.vue";
import Card from "@/components/base/Card.vue";
export default {
  components: {
    Hero,
    Card,
  },
};
</script>
<style scoped>
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
</style>
