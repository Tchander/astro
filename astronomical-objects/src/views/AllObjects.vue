<template>
  <div>
    <router-link class="back-to-home" to="/">Home</router-link>
    <div class="selectors">
      <filter-by-type v-on:filter-by-type="filterByType"/>
      <filter-by-characteristic v-on:filter-by-characteristics="filterByCharacteristics"/>
    </div>
    <object-list v-bind:objects="filteredObjectsByType"/>
  </div>
</template>

<script>
import ObjectList from '@/components/ObjectList'
import FilterByType from "@/components/FilterByType"
import FilterByCharacteristic from "@/components/FilterByCharacteristic"
export default {
  data() {
    return {
      allObjects: [
        {
          id: 1, name: 'Sun', objectType: 'Star', massKg: 1.9885e+30, radiusKm: 695700, densityGCm3: 1.408,
          rotationPeriodDays: 25.05, temperatureK: 5772, knownPlanets: 8, typeOfStar: 'G2V',
          descriptionOfType: 'Yellow Dwarf', age: 4.6e+9, distanceToTheSunLY: 0, rightAscensionH: 0, rightAscensionM: 0,
          rightAscensionS: 0, declinationD: 0, declinationM: 0, declinationS: 0
        },
        {
          id: 2, name: 'Jupiter', objectType: 'Planet', massKg: 1.8982e+27, radiusKm: 69911, densityGCm3: 1.326,
          rotationPeriodDays: 0.41375, temperatureK: 139, knownSatellites: 79, orbitalParent: 'Sun',
          aphelionKm: 816.62e+6, perihelionKm: 740.52e+6, semiMajorAxisKm: 778.57e+6, orbitalPeriodDays: 4332.59,
          eccentricity: 0.0489, inclination: 1.303, argumentOfPerihelion: 273.867, longitudeOfAscendingNode: 100.464,
          meanAnomaly: 20.020, albedo: 0.538
        },
        {
          id: 3, name: 'Earth', objectType: 'Planet', massKg: 5.97237e+24, radiusKm: 6371, densityGCm3: 5.514,
          rotationPeriodDays: 0.99726968, temperatureK: 287.16, knownSatellites: 1, orbitalParent: 'Sun',
          aphelionKm: 152100000, perihelionKm: 147095000, semiMajorAxisKm: 149598023, orbitalPeriodDays: 365.256363004,
          eccentricity: 0.0167086, inclination: 0.00005, argumentOfPerihelion: 114.20783,
          longitudeOfAscendingNode: -11.26064, meanAnomaly: 358.617, albedo: 0.367
        },
        {
          id: 4, name: 'Moon', objectType: 'Satellite', massKg: 7.342e+22, radiusKm: 1737.4, densityGCm3: 3.344,
          rotationPeriodDays: 27.321661, temperatureK: 250, knownSatellites: 0, orbitalParent: 'Earth',
          aphelionKm: 405400, perihelionKm: 362600, semiMajorAxisKm: 384399, orbitalPeriodDays: 27.321661,
          eccentricity: 0.0549, inclination: 5.145, argumentOfPerihelion: 'unknown',
          longitudeOfAscendingNode: 'unknown', meanAnomaly: 'unknown', albedo: 0.136
        },
        {
          id: 5, name: 'Ganymede', objectType: 'Satellite', massKg: 1.4819e+23, radiusKm: 2634.1, densityGCm3: 1.936,
          rotationPeriodDays: 7.15455296, temperatureK: 110, knownSatellites: 0, orbitalParent: 'Jupiter',
          aphelionKm: 1071600, perihelionKm: 1069200, semiMajorAxisKm: 1070400, orbitalPeriodDays: 7.15455296,
          eccentricity: 0.0013, inclination: 0.20, argumentOfPerihelion: 'unknown', longitudeOfAscendingNode: 'unknown',
          meanAnomaly: 'unknown', albedo: 0.43
        },
        {
          id: 6, name: 'Pluto', objectType: 'Dwarf planet', massKg: 1.303e+22, radiusKm: 1188.3, densityGCm3: 1.854,
          rotationPeriodDays: 6.387230, temperatureK: 44, knownSatellites: 5, orbitalParent: 'Sun',
          aphelionKm: 7.37593e+9, perihelionKm: 4.43682e+9, semiMajorAxisKm: 5.90638e+9, orbitalPeriodDays: 90560,
          eccentricity: 0.2488, inclination: 17.16, argumentOfPerihelion: 113.834, longitudeOfAscendingNode: 110.299,
          meanAnomaly: 14.53, albedo: 0.58
        },
        {
          id: 7, name: 'Ceres', objectType: 'Dwarf planet', massKg: 9.3835e+20, radiusKm: 469.73, densityGCm3: 2.162,
          rotationPeriodDays: 0.377917, temperatureK: 133, knownSatellites: 0, orbitalParent: 'Sun',
          aphelionKm: 445749000, perihelionKm: 382774000, semiMajorAxisKm: 414261000, orbitalPeriodDays: 1683.14570801,
          eccentricity: 0.07600902910, inclination: 10.59406704, argumentOfPerihelion: 73.5976941,
          longitudeOfAscendingNode: 80.3055316, meanAnomaly: 77.37209589, albedo: 0.09
        },
        {
          id: 8, name: 'Vesta', objectType: 'Asteroid', massKg: 2.59076e+20, radiusKm: 262.7, densityGCm3: 3.456,
          rotationPeriodDays: 0.2226, temperatureK: 163,  knownSatellites: 0, orbitalParent: 'Sun',
          aphelionKm: 384672972.760566, perihelionKm: 321966033.299247, semiMajorAxisKm: 353318755.040553,
          orbitalPeriodDays: 1325.75, eccentricity: 0.08874, inclination: 7.14043, argumentOfPerihelion: 151.19853,
          longitudeOfAscendingNode: 103.85136, meanAnomaly: 20.86384, albedo: 0.423
        },
        {
          id: 9, name: 'Hygiea', objectType: 'Asteroid', massKg: 8.32e+19, radiusKm: 217, densityGCm3: 1.94,
          rotationPeriodDays: 0.57625, temperatureK: 164, knownSatellites: 0, orbitalParent: 'Sun',
          aphelionKm: 522814638.52235997, perihelionKm: 417108783.0857399, semiMajorAxisKm: 469961710.80404997,
          orbitalPeriodDays: 2033.8, eccentricity: 0.1125, inclination: 3.8316, argumentOfPerihelion: 312.32,
          longitudeOfAscendingNode: 283.20, meanAnomaly: 152.18, albedo: 0.0717
        },
        {
          id: 10, name: 'Proxima Centauri', objectType: 'Star', massKg: 1.9885e+30*0.1221, radiusKm: 695700*0.1542,
          densityGCm3: 'unknown', rotationPeriodDays: 82.6, temperatureK: 3042, knownPlanets: 3, typeOfStar: 'M5.5Ve',
          descriptionOfType: 'Red dwarf', age: 4.85e+9, distanceToTheSunLY: 4.2465, rightAscensionH: 14,
          rightAscensionM: 29, rightAscensionS: 42.94853, declinationD: -60, declinationM: 40, declinationS: 46.1631
        },
        {
          id: 11, name: 'Proxima Centauri b', objectType: 'Planet', massKg: 5.97237e+24*1.60, radiusKm: 6371*1.30,
          densityGCm3: 'unknown', rotationPeriodDays: 'unknown', temperatureK: 234, knownSatellites: 0,
          orbitalParent: 'Proxima Centauri', aphelionKm: 'unknown', perihelionKm: 'unknown',
          semiMajorAxisKm: 7255496.728949999, orbitalPeriodDays: 11.18427, eccentricity: 0.124, inclination: 'unknown',
          argumentOfPerihelion: 310, longitudeOfAscendingNode: 'unknown',meanAnomaly: 'unknown', albedo: 'unknown'
        },
        {
          id: 12, name: '2002 VR128', objectType: 'Asteroid', massKg: 'unknown', radiusKm: 224.25,
          densityGCm3: 'unknown', rotationPeriodDays: 'unknown', temperatureK: 44, knownSatellites: 0,
          orbitalParent: 'Sun', aphelionKm: 7427534280.254999, perihelionKm: 4338188652.429299,
          semiMajorAxisKm: 5882936265.2775, orbitalPeriodDays: 90072.7, eccentricity: 0.26257, inclination: 14.040,
          argumentOfPerihelion: 287.87, longitudeOfAscendingNode: 23.152, meanAnomaly: 73.453, albedo: 0.052
        }
      ],
      filteredObjectsByType: [],
      filteredObjectsByCharacteristic: []
    }
  },
  components: {
    FilterByCharacteristic,
    FilterByType,
    ObjectList
  },
  methods: {
    filterByType(filter) {
      const mapper = {
        'stars': 'Star',
        'planets': 'Planet',
        'dwarf-planets': 'Dwarf planet',
        'satellites': 'Satellite',
        'asteroids': 'Asteroid'
      }
      if (Object.keys(mapper).includes(filter)) {
        this.filteredObjectsByType = this.allObjects.filter(t => t.objectType === mapper[filter])
        return
      }
      this.filteredObjectsByType = this.allObjects
    },
    filterByCharacteristics(filter) {
      const mapper = {
        'radius': 'radiusKm',
        'mass': 'massKg',
        'density': 'densityGCm3',
        'temperature': 'temperatureK'
      }
      if (Object.keys(mapper).includes(filter)) {
        this.filteredObjectsByCharacteristic =
            this.filteredObjectsByType.sort((prev, next) => {
              let result
              if (typeof next[mapper[filter]] === 'string') {
                next[mapper[filter]] = Number.NEGATIVE_INFINITY
              }
              if (typeof prev[mapper[filter]] === 'string') {
                prev[mapper[filter]] = Number.NEGATIVE_INFINITY
              }
              result = next[mapper[filter]] - prev[mapper[filter]]
              if (next[mapper[filter]] === Number.NEGATIVE_INFINITY) {
                next[mapper[filter]] = 'unknown'
              }
              if (prev[mapper[filter]] === Number.NEGATIVE_INFINITY) {
                prev[mapper[filter]] = 'unknown'
              }
              return result
            })
      }

    },
    sortBy (value, prev, next) {
      console.log(value)
      return next[value] - prev[value]
    }
  },
  created() {
    this.filteredObjectsByType = this.allObjects
  }
}
</script>

<style>
.back-to-home {
  position: fixed;
  top: 50px;
  right: 50px;
}
.selectors {
  margin: 50px auto;
}
.select {
  width: 10%;
  background: none;
  margin: 0 20px;
  color: red;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
