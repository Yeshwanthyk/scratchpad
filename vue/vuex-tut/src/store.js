import Vue from "vue";
import Vuex from "vuex";
import EventService from "./services/EventService.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: { id: "abc123", name: `Adam` },
    categories: [
      "sustainability",
      "nature",
      "animal welfare",
      "housing",
      "education",
      "food",
      "community",
    ],
    events: [],
  },
  mutations: {
    ADD_EVENT(state, event) {
      state.events.push(event);
    },
  },
  actions: {
    createEvent({ commit }, event) {
      // save to mock db
      EventService.postEvent(event);
      // commit mutation
      commit("ADD_EVENT", event);
    },
  },
  getters: {
    catLength: (state) => {
      return state.categories.length;
    },
  },
});
