<template>
  <div>
    <v-card elevation="20" max-width="100%" color="">
      <v-card-title class="ms-4">
        <span class="mt-5 text-h6 font-weight-bold">프로필 수정</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col>
              <v-file-input
                v-model="profileImage"
                label="프로필 사진을 올려주세요!"
                filled clearable color="purple lighten-2"
                dense clear-icon="mdi-close-circle"
                prepend-icon="mdi-camera"
              ></v-file-input>
            </v-col>
            <v-col cols="12">
              <v-container fluid>
                <v-textarea
                  v-model="newIntroduction"
                  clearable color="purple lighten-2"
                  clear-icon="mdi-close-circle"
                  label="자기소개를 적어주세요🤩"
                ></v-textarea>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="black darken-1"
          text class="me-0"
          @click="closeDialog"
        >
          Close
        </v-btn>
        <v-btn
          color="purple darken-1"
          text class="ms-0"
          @click="onSubmit"
        >
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ProfileForm',
  data() {
    return {
      profileImage: null,
      newIntroduction: this.introduction,
    }
  },
  props: {
    username: String,
    introduction: String,
  },
  methods: {
    ...mapActions(['updateProfile']),
    closeDialog() {
      this.$emit('close-dialog')
    },
    onSubmit() {
      const profileData = {
        username: this.username,
        profileImage: this.profileImage,
        introduction: this.newIntroduction,
      }
      this.updateProfile(profileData)
      this.closeDialog()
    },
  }
}
</script>

<style>

</style>