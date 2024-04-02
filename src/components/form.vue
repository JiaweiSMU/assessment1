<template>
    <form @submit.prevent="submitAuthor">
        <label>
            Author name:
            <!-- v-model to bind the input field to authorName
            ,required to ensure the field is not empty -->
            <input type="text" v-model="authorName" required />
        </label>
        <button type='submit'>Submit</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            authorName: ''
        }
    },
    methods: {
        submitAuthor() {
            console.log(this.authorName);
            // Emit the submit event with the author name
            this.$emit('submit', this.authorName);
            // Clear the input field
            this.authorName = ''; 
        }
    }
}
</script>