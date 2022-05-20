<template>
  <v-row>
    <v-col>
      <v-sheet height="500">
        <v-btn
          fab
          text
          small
          color="grey darken-2"
          @click="prev"
        >
          <v-icon small>
            mdi-chevron-left
          </v-icon>
        </v-btn>
        <v-btn
          fab
          text
          small
          color="grey darken-2"
          @click="next"
        >
          <v-icon small>
            mdi-chevron-right
          </v-icon>
        </v-btn>
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          @click:date="clickDate"
        >
        </v-calendar>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'MovieCalendar',
    data: () => {
      const date = new Date()
      return {
        today: date.now,
        colors: ['#1867c0', '#fb8c00', '#000000'],
        category: ['Development', 'Meetings', 'Slacking'],
    }},
    mounted () {
      this.$refs.calendar.checkChange()
    },
    methods: {
      prev () {
        console.log(this.$refs.calendar)
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      clickDate () {
        console.log(this)
      },
    },
  }
</script>

<style>

</style>