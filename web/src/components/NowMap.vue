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
    import {onBeforeMount, onMounted, ref, watch } from 'vue'
    import { AdvancedMarker, Polyline, GoogleMap } from 'vue3-google-map'

    const dashiCenter = ref({ lat: 35.85697259477041, lng: 139.6145971391871 })
    const dashiMarkerOptions = ref({ position: dashiCenter.value })
    const lng = ref(139.614076)
    const mapMarkers = ref(null)
    const i = ref(0)
    const apikey = import.meta.env.VITE_GOOGLE_API_KEY
    const cfClientSecret = import.meta.env.VITE_CF_SECRET
    const cfClientId = import.meta.env.VITE_CF_ID
    const markerStandby = ref(false)

    onBeforeMount(async () => {
      try{
        const response = await fetch('https://gpsapi.marpyong.work/',
          {
            method: 'GET',
            mode: 'cors',
            credentials: 'same-origin',
            headers: {
                'CF-Access-Client-Secret': cfClientSecret,
                'CF-Access-Client-Id': cfClientId,
                'Access-Control-Allow-Origin': 'https://dojo-summer.marpyong.work',
            }
          }
        )
        if(!response.ok){
            throw new Error('データの取得に失敗しました')
        }
        dashiCenter.value = await response.json()
        console.log('受信したデータ:', dashiCenter.value)

      } catch(error) {
        console.log(error)
      }
    })

    onMounted(() => {
      setInterval(async () => {
        try{
          const response = await fetch('https://gpsapi.marpyong.work/',
          {
            method: 'GET',
            mode: 'cors',
            credentials: 'same-origin',
            headers: {
              'CF-Access-Client-Secret': cfClientSecret,
              'CF-Access-Client-Id': cfClientId,
              'Access-Control-Allow-Origin': 'https://dojo-summer.marpyong.work',
            }
          })
          if(!response.ok){
            throw new Error('データの取得に失敗しました')
          }
          dashiCenter.value = await response.json()
          console.log('受信したデータ:', dashiCenter.value)
        } catch(error) {
            console.log(error)
        }
      }, 10_000)
    })
    watch(dashiCenter, () => {
        mapMarkers.value.marker.position = dashiCenter.value
        // console.log(dashiMarkerOptions.value.position)
        // console.log(mapMarkers.value.marker)
        return
    })
</script>
