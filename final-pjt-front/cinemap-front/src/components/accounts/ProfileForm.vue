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
                v-model="profileImage"
                label="프로필 사진"
                filled
                prepend-icon="mdi-camera"
              ></v-file-input>
            </v-col>
            <v-col cols="12">
              <v-container fluid>
                <v-textarea
                  v-model="newIntroduction"
                  clearable
                  clear-icon="mdi-close-circle"
                  label="Text"
                ></v-textarea>
              </v-container>
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