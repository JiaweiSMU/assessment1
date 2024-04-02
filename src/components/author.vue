<template>
    <div>
        <ul>
            <li v-for="author in authors">
                {{ author }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: {
        authors: {
            type: Array,
            required: true
        }
    }
}
</script>