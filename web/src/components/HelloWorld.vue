<template>
  <v-app id="inspire">
      <v-row>
        <v-col cols="4">
          <v-container class="d-flex">
            <v-badge location='bottom end' content="配信" offsetX="10">
              <v-btn icon @click="scrollTostreamTarget" class="ma-1">
                <v-icon>mdi-antenna</v-icon>
              </v-btn>
            </v-badge>
            <v-badge location='bottom end' content="現在値" offsetX="10">
              <v-btn icon @click="scrollToNowMapTarget" class="ma-1">
                <v-icon>mdi-map-marker-radius </v-icon>
              </v-btn>
            </v-badge>
          </v-container>
        </v-col>       
        <v-col cols="8">
          <v-container class="algin-right">
            <p class="text-right text-body-2">さいたま市 桜区 道場自治会</p>
            <h5 class="text-h5 text-right">道場地区夏祭り2025</h5>
          </v-container>
        </v-col>
      </v-row>

      <v-main>
        <v-spacer style="height: 300px;" />
        <div class="ma-6">
          <v-row>
            <v-col cols="12" lg="3">
              <p class="text-h4">道場地区夏祭り2025</p>
            </v-col>
            <v-col cols="12" lg="9">
              <p class="text-h4">非公式info</p>
            </v-col>
          </v-row>
          <p class="font-italic">夏を彩る 五穀豊穣 願いの場</p>
        </div>
        <v-spacer style="height: 300px;" />
        <v-card class="ma-6">
          <v-card-title>開催概要</v-card-title>
          <v-card-text>
            <p>開催日: 2025年7月13日 (日) 12:00頃から 18:00頃まで(予定)</p>
            <p>場所: 道場一丁目～五丁目 各所を巡回します</p>
            <p>詳細は後日発表します。</p>
          </v-card-text>
        </v-card>
        <v-row class="ma-3">
          <v-col cols="12" lg="6">
            <div ref="streamTarget">
              <v-card>
                <v-card-title>動画配信 (試験施策)</v-card-title>
                <v-card-text>
                  <p>YouTubeにて、山車からの様子を配信しています。</p>
                  <p>※ 限定公開ですので必要以上の拡散は控えていただくようにお願いします。</p>
                  <iframe 
                    width="100%" 
                    height="473" 
                    src="https://www.youtube.com/embed/Blf-ZH2RIh8?si=h5OZGFj32GUxuLbx" 
                    title="YouTube video player" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    referrerpolicy="strict-origin-when-cross-origin" 
                    allowfullscreen></iframe>
                </v-card-text>
              </v-card>
            </div>
          </v-col>
          <v-col cols="12" lg="6">
            <div ref="nowMapTarget">
              <v-card :key="dashiMarkerOptions">
                <v-card-title>お祭りいまココ！</v-card-title>
                <v-card-text>
                  <p>山車や御神輿のだいたいの現在位置をコチラに表示します。</p>
                  <NowMap></NowMap>
                </v-card-text>
              </v-card>
            </div>
          </v-col>
        </v-row>
        <v-card class="ma-6">
          <v-card-title>巡回経路</v-card-title>
          <v-card-text>
            <p>このような経路で巡回をする予定です。</p>
            <p>ご参考にしてください。</p>
                <GoogleMap
                  ref="mapMarkers"
                  :api-key="apikey"
                  :center="center"
                  map-id="35108337d549f3c28a9dacfb"
                  style="width: 100%; height: 500px"
                  :zoom="16"
                >
                  <AdvancedMarker :options="markerOptions" />
                  <AdvancedMarker :options="markerOptions">
                    <div style="background: white; color: black; padding: 5px; border-radius: 5px">
                      起点・終点
                    </div>
                  </AdvancedMarker>
                  <Polyline :options="dashiPath" />
                </GoogleMap>
          </v-card-text>
        </v-card>
      </v-main>
      <v-footer app height="40">
        <div class="flex-grow-1"></div>
        <div class="font-weight-thin">&copy; {{ new Date().getFullYear() }} さいたま市 桜区 道場囃子連 電脳処</div>
      </v-footer>
  </v-app>
</template>

<script setup>
  import { onMounted, ref, watch } from 'vue'
  import { AdvancedMarker, Polyline, GoogleMap } from 'vue3-google-map'

  const center = ref({ lat: 35.85697259477041, lng: 139.6145971391871 })
  const markerOptions = ref({ position: center.value, title: 'Start Stop'})
  const apikey = ref(import.meta.env.VITE_GOOGLE_API_KEY)
  const overlayModel = ref(true)

  const mapMarkers = ref()
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
  const dashiPath = {
      path: dashiPlan,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2,
    }

  const streamTarget = ref(null)
  const scrollTostreamTarget = () => {
    if (streamTarget.value) {
      streamTarget.value.scrollIntoView({
        behavior: 'smooth',
      })
    }
  }

  const nowMapTarget = ref(null)
  const scrollToNowMapTarget = () => {
    if (nowMapTarget.value) {
      nowMapTarget.value.scrollIntoView({
        behavior: 'smooth',
      })
    }
  }

</script>

<script>
  export default {
    data: () => ({ drawer: null }),
  }
</script>
