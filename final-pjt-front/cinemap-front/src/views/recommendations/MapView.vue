<template>
  <div class="distribution-map">
    <img src="@/assets/worldmapcolor.png" alt="" />
    <font-awesome-icon icon="fa-solid fa-location-dot" />
    <button class="map-point" style="top:15%;left:35%">
      <div class="content">
        <div class="centered-y">
          <h2>A Place</h2>
          <p>You can put plenty of details in here. In the original, I listed contact information and linked phone numbers and email addresses.</p>
        </div>
      </div>
    </button>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
div, img {
  position: relative;
  box-sizing: border-box;
}

p {
  font-size: 12pt;
  margin-bottom: 12pt;
}

.centered-y {
  position: absolute;
  width: 100%;
  top: 50%;
  transform: translateY(-50%);
}

.distribution-map {
  position: relative;
  width: 70%;
  padding: 20px;
  box-sizing: border-box;
  margin: 0 auto;
}
.distribution-map > img {
  width: 100%;
  position: relative;
  margin: 0;
  padding: 0;
}
.distribution-map .map-point {
  cursor: pointer;
  outline: none;
  z-index: 0;
  position: absolute;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=80);
  opacity: 0.8;
  transform: translate(-50%, -50%);
  -moz-transition: opacity 0.25s ease-in-out 0.25s, width 0.25s ease-in-out 0.25s, height 0.25s ease-in-out 0.25s, z-index 0.25s ease-in-out 0.25s;
  -o-transition: opacity 0.25s ease-in-out 0.25s, width 0.25s ease-in-out 0.25s, height 0.25s ease-in-out 0.25s, z-index 0.25s ease-in-out 0.25s;
  -webkit-transition: opacity 0.25s ease-in-out, width 0.25s ease-in-out, height 0.25s ease-in-out, z-index 0.25s ease-in-out;
  -webkit-transition-delay: 0.25s, 0.25s, 0.25s, 0.25s;
  transition: opacity 0.25s ease-in-out 0.25s, width 0.25s ease-in-out 0.25s, height 0.25s ease-in-out 0.25s, z-index 0.25s ease-in-out 0.25s;
  background: rgba(26, 26, 26, 0.85);
  border: 5px solid #7fcff7;
}
.distribution-map .map-point .content {
  filter: progid:DXImageTransform.Microsoft.Alpha(Opacity=0);
  opacity: 0;
  transition: opacity 0.25s ease-in-out;
  width: 100%;
  height: 100%;
  left: 50%;
  transform: translateX(-50%);
  overflow: overlay;
}
.distribution-map .map-point:active, .distribution-map .map-point:focus {
  margin: 0;
  padding: 0;
  filter: progid:DXImageTransform.Microsoft.Alpha(enabled=false);
  opacity: 1;
  width: 300px;
  height: 220px;
  color: #e5e5e5;
  z-index: 1;
  transition: opacity 0.25s ease-in-out, width 0.25s ease-in-out, height 0.25s ease-in-out;
}
.distribution-map .map-point:active .content, .distribution-map .map-point:focus .content {
  filter: progid:DXImageTransform.Microsoft.Alpha(enabled=false);
  opacity: 1;
  -moz-transition: opacity 0.25s ease-in-out 0.25s, height 0.25s ease-in-out, overflow 0.25s ease-in-out;
  -o-transition: opacity 0.25s ease-in-out 0.25s, height 0.25s ease-in-out, overflow 0.25s ease-in-out;
  -webkit-transition: opacity 0.25s ease-in-out, height 0.25s ease-in-out, overflow 0.25s ease-in-out;
  -webkit-transition-delay: 0.25s, 0s, 0s;
  transition: opacity 0.25s ease-in-out 0.25s, height 0.25s ease-in-out, overflow 0.25s ease-in-out;
  overflow: hidden;
}
.distribution-map .map-point:active .content a:hover, .distribution-map .map-point:active .content a:active, .distribution-map .map-point:focus .content a:hover, .distribution-map .map-point:focus .content a:active {
  color: #afe1fa;
}

</style>