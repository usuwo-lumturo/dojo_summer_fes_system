<template>
    <GoogleMap
        :api-key="apikey"
        :center="dashiCenter"
        map-id="35108337d549f3c28a9dacfb"
        style="width: 100%; height: 500px"
        :zoom="18"
    >
    <AdvancedMarker ref="mapMarkers" :options="dashiMarkerOptions" />
    </GoogleMap>
</template>

<script setup>
    import { onMounted, ref, watch } from 'vue'
    import { AdvancedMarker, Polyline, GoogleMap } from 'vue3-google-map'

    const dashiCenter = ref({ lat: 35.85697259477041, lng: 139.6145971391871 })
    const dashiMarkerOptions = ref({ position: dashiCenter.value })
    const lng = ref(139.614076)
    const mapMarkers = ref(null)
    const i = ref(0)
    const apikey = import.meta.env.VITE_GOOGLE_API_KEY

    const dashiPlan = [
            { lat: 35.856911973499116, lng: 139.6146238763262 },
            { lat: 35.85698182898782, lng: 139.61490646647718 },
            { lat:35.857945009360805, lng:139.6148362515459 },
            { lat:35.858284129994196, lng:139.61632219530097 },
            { lat:35.859071058156644, lng:139.61596277931994 },
            { lat:35.858284129994196, lng:139.61632219530097 },
            { lat:35.85610746470744, lng:139.61653724298023 },
            { lat:35.85609968811247, lng:139.6161539716762 },
            { lat:35.854789495589486, lng:139.61638255213094 },
            { lat:35.854623037083, lng:139.61545774388418 },
            { lat:35.85511598344347, lng:139.61462351564316 },
            { lat:35.855440439620665, lng:139.6146069508192 },
            { lat:35.8559013888588, lng:139.61443025939712 },
            { lat:35.856248217832736, lng:139.6143198272546 },
            { lat:35.85570895406929, lng:139.6128814486467 },
            { lat:35.85604683346354, lng:139.61247008886676 },
            { lat:35.856563719012, lng:139.6120007522622 },
            { lat:35.85693515850038, lng:139.61270751797989 },
            { lat:35.857725021013515, lng:139.61214155321662 },
            { lat:35.85830902195032, lng:139.61169982466032 },
            { lat:35.8585976644976, lng:139.61159491412843 },
            { lat:35.85914585870665, lng:139.61331213393865 },
            { lat:35.85784137404557, lng:139.6141541790269 },
            { lat:35.857953251772685, lng:139.61482781508934 },
            { lat:35.856984385290296, lng:139.61488303116096 },
            { lat:35.856888169266625, lng:139.61457658197574 },
    ]

    onMounted(() => {
        setInterval(() => {
            if(i.value < dashiPlan.length){
                dashiCenter.value = dashiPlan[i.value]
                i.value = i.value + 1
            }
        }, 3_000)
    })
    watch(dashiCenter, () => {
        mapMarkers.value.marker.position = dashiCenter.value
        // console.log(dashiMarkerOptions.value.position)
        // console.log(mapMarkers.value.marker)
        return
    })
</script>