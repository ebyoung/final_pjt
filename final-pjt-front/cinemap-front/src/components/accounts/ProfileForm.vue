<template>
  <div>
    <v-card>
      <v-card-title>
        <span class="text-h5">프로필 수정</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col>
              <v-file-input
                label="프로필 사진"
                filled
                prepend-icon="mdi-camera"
              ></v-file-input>
            </v-col>
            <v-col cols="12">
              <v-text-field
                label="자기 소개"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="blue darken-1"
          text
          @click="closeDialog"
        >
          Close
        </v-btn>
        <v-btn
          color="blue darken-1"
          text
          @click="closeDialog"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'ProfileForm',
  methods: {
    closeDialog() {
      this.$emit('close-dialog')
    },
  }
}
</script>

<style>

</style>