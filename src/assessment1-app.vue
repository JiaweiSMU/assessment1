<template>
  <div id="app">
    <h1>Author Form</h1>
    <!-- Vue Component, @submit is a event listener,
    listening for submit event -->
    <aForm @submit="addAuthor" />
    <h1>Author List</h1>
    <!-- Pass a authors prop value to authorList,
    vbind it to author -->
    <authorList :authors="authors" />
    <!-- Display Retrieved User -->
    <!-- Table -->
    <!-- Check if users is not empty -->
    <div v-if="users.length > 0">
      <h1>Users</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Company</th>
          </tr>
        </thead>
        <tbody>
          <!-- Loop through users array, display user data -->
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.address.street + ', ' + user.address.city + ', ' + user.address.zipcode }}</td>
            <td>{{ user.company.name + ', ' + user.company.catchPhrase }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import aForm from './components/form.vue'
import authorList from './components/author.vue'
import axios from 'axios'

export default {
  components: {
    aForm,
    authorList
  },
  data() {
    return {
      authors: [],
      users: []
    }
  },

  created() {
    this.fetchUsers()
  },

  methods: {
    addAuthor(authorName) {
      console.log(authorName);
      // Emit the submit event from being pushed to array
      // because the component @submit will send over submit event
      if (!(authorName instanceof Event)) {
        this.authors.push(authorName);
      }
    },

    fetchUsers() {
      axios.get('http://localhost:5001/getUsers').then(response => {
        // this gets the data, which is an array
        this.users = response.data
        console.log(response.data)
      })
        .catch(error => {
          if (error.response) {
            this.users = []
            console.log(error)
          }

        })
    },
  }
}
</script>