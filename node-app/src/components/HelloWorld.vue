<template>
  <v-container class="fill-height" max-width="900">
    <div>
      <v-row>
        <v-col cols="12">
          <v-card
            class="py-4"
            color="surface-variant"
            image="https://cdn.vuetifyjs.com/docs/images/one/create/feature.png"
            prepend-icon="mdi-rocket-launch-outline"
            rounded="lg"
            variant="tonal"
          >
          <v-card-title>道場地区 御神輿位置情報登録用サイト</v-card-title>
          <v-card-text>そういうやつです</v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card>
            <v-card-title>位置情報</v-card-title>
            <v-card-text>
              <p> 緯度(latitude):{{ current.lat }}</p>
              <p> 経度(longitude):{{ current.lng }}</p>
              <GoogleMap
                :api-key="apikey"
                :center="dashiCenter"
                map-id="35108337d549f3c28a9dacfb"
                style="width: 100%; height: 500px"
                :zoom=18
              >
                <AdvancedMarker ref="mapMarkers" :options="dashiMerkerOptions" />
              </GoogleMap>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup>
  import { ref, onBeforeMount, onMounted, watch} from 'vue'
  import VueGeolocation from 'vue3-geolocation'
  import { AdvancedMarker, GoogleMap } from 'vue3-google-map'

  const dashiCenter = ref({ lat: 35.856911973499116, lng: 139.6146238763262 })
  const dashiMerkerOptions = ref({ position: dashiCenter.value })
  const mapMarkers = ref(null)
  const apikey = import.meta.env.VITE_GOOGLE_API_KEY

  //現在地情報を取得する関数を用意
  const current = ref({
          //position: undefined,
          lat: undefined,
          lng: undefined,
          getLocation: () => {
              VueGeolocation.getLocation()
                  .then((coordinates) => {
                      current.value.position = coordinates
                      current.value.lat = coordinates.lat  //緯度
                      current.value.lng = coordinates.lng  //経度
                  })
                  .catch((error) => {
                      console.log(error)
                  })
          },
      })

  const connection = new WebSocket('wss://dojopositon.marpyong.work/ws')

  const getLocateAndSend = () => {
      current.value.getLocation() // 定期的に位置情報を更新
      if (connection.readyState === WebSocket.OPEN) {
        connection.send(JSON.stringify(current.value))
      }
  }

  //ページが読み込まれると同時に関数を呼び出す
  onBeforeMount(() => {
    current.value.getLocation()
    // WebSocket接続を確立してデータを送信
    connection.onopen = () => {
          console.log('WebSocket connection established')
    }
  })

  watch(current, (newValue, oldValue) => {
    console.log('位置情報が更新されました:', JSON.stringify(newValue))
    mapMarkers.value.marker.position = newValue.position
    dashiCenter.value = newValue.position
  }, { deep: true })

  onMounted(() => {
    getLocateAndSend()
    // WebSocket接続が開かれたときに位置情報を送信
    setInterval(() => {
      getLocateAndSend()
    }, 3000) // 5秒ごとに位置情報を送信
  })

</script>
