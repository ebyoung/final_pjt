<template>
  <div class="calendar">
      <div class="header">
          <div class="year-month" >{{ viewYear }}년 {{ viewMonth + 1 }}월</div>
          <div class="nav">
              <button class="nav-btn go-prev" @click="prevMonth">&lt;</button>
              <button class="nav-btn go-today" @click="goToday">Today</button>
              <button class="nav-btn go-next" @click="nextMonth">&gt;</button>
          </div>
      </div>
      <div class="main">
          <div class="days">
              <v-card
                elevation="3"
                outlined
                tile
                class="day"
                v-for="(day, idx) in ['일', '월', '화', '수', '목', '금', '토']" :key="idx"
              >{{ day }}</v-card>
          </div>
          <div class="dates">
            <v-card
              elevation="3"
              outlined
              tile
              width="calc(100% / 7)"
              height="167.5px"
              class="prevDates"
              v-for="(date, idx) in prevDates" :key="idx*10+10"
            >
              <p>{{ date }}</p>
              <DayReview :date="`${viewYear}-${viewMonth<9 ? `0${viewMonth}`: viewMonth }-${date<10 ? `0${date}`:date}`" :idx="idx" class="m-5"/>
            </v-card>
            <v-card
              elevation="3"
              outlined
              tile
              width="calc(100% / 7)"
              height="167.5px"
              class="thisDates"
              v-for="(date, idx) in thisDates" :key="idx*100+100"
            >
              <p>{{ date }}</p>
              <DayReview :date="`${viewYear}-${viewMonth<9 ? `0${viewMonth+1}`: viewMonth+1 }-${date<10 ? `0${date}`:date}`" :idx="idx" class="m-5"/>
            </v-card>
            <v-card
              elevation="3"
              outlined
              tile
              width="calc(100% / 7)"
              height="167.5px"
              class="nextDates"
              v-for="(date, idx) in nextDates" :key="idx"
            >
              <p>{{ date }}</p>
              <DayReview
              :date="`${viewYear}-${viewMonth<9 ? `0${viewMonth+2}`: viewMonth+2 }-${date<10 ? `0${date}`:date}`"
              :idx="idx" class="m-5"/>
            </v-card>
          </div>
      </div>
  </div>
</template>

<script>
import DayReview from '@/components/accounts/DayReview.vue'

export default {
  name: 'MovieCalendar',
  components: {
    DayReview,
  },
  data() {
    const date =  new Date()
    return {
      viewYear: date.getFullYear(),
      viewMonth: date.getMonth(),
      prevDates: [],
      thisDates: [],
      nextDates: [],
    }
  },
  methods: {
    renderCalendar() {
      // 지난 달 마지막 Date, 이번 달 마지막 Date
      const prevLast = new Date(this.viewYear, this.viewMonth, 0)
      const thisLast = new Date(this.viewYear, this.viewMonth + 1, 0)

      const PLDate = prevLast.getDate()
      const PLDay = prevLast.getDay()

      const TLDate = thisLast.getDate()
      const TLDay = thisLast.getDay()

      // Dates 기본 배열들
      const prevDates = [];
      const thisDates = [...Array(TLDate + 1).keys()].slice(1)
      const nextDates = [];

      // prevDates 계산
      if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
          prevDates.unshift(PLDate - i)
        }
      }

      // nextDates 계산
      for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i)
      }

      // Dates 합치기
      // const dates = prevDates.concat(thisDates, nextDates)
      this.prevDates = prevDates
      this.thisDates = thisDates
      this.nextDates = nextDates

      // // 이번 달의 구간 확인
      // const firstDateIndex = dates.indexOf(1)
      // const lastDateIndex = dates.lastIndexOf(TLDate)

    },
    prevMonth() {
      const prevM = this.viewMonth - 1
      if (prevM < 0) {
        this.viewMonth = 11
        this.viewYear -= 1
      } else {
        this.viewMonth -= 1
      }
      this.renderCalendar()
    },
    nextMonth() {
      const prevM = this.viewMonth + 1
      this.viewMonth = prevM % 12
      this.viewYear += parseInt(prevM / 12)
      this.renderCalendar()
    },
    goToday() {
      this.viewMonth = new Date().getMonth()
      this.viewYear = new Date().getFullYear()
      this.renderCalendar()
    },
  },
  created() {
    this.renderCalendar()
  }
}

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.calendar {
  width: 800px;
  margin: 50px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.year-month {
  font-size: 35px;
}

.nav {
  display: flex;
  border: 1px solid #333333;
  border-radius: 5px;
}

.nav-btn {
  width: 28px;
  height: 30px;
  border: none;
  font-size: 16px;
  line-height: 34px;
  background-color: transparent;
  cursor: pointer;
}

.go-today {
  width: 75px;
  border-left: 1px solid #333333;
  border-right: 1px solid #333333;
}

.days {
  display: flex;
  margin: 25px 0 0;
}

.day {
  width: calc(100% / 7);
  aspect-ratio: 2.5/1;
  text-align: center;
  padding-top: 1.5%;
}

.dates {
  display: flex;
  flex-flow: row wrap;
}

p {
  width: 20%;
  position: absolute;
  background: white;
  text-align: center;
  font-weight: bolder;
  z-index: 2;
}

.prevDates > p,
.nextDates > p {
  color: gray;
  font-weight: normal;
}
</style>