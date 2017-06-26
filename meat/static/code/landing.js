document.addEventListener("DOMContentLoaded", function (event) {
    //do work

    console.log('finished loading')


    app = new Vue({
        el: '#app',
        data: {
            message: 'Hello Vue!',
            selectedSuburb: '',
            selectedPostcode: '',
            animals: [ 'beef', 'pork', 'poultry' ],
            availableHomeSuburbs: [],
            availableWorkSuburbs: []
        },
        methods: {
            displayDropDown: function() {
                return app.$data.availableSuburbs.length > 0;
            },
            clearAnimalSearch: function() {

            }
        },
        watch: {
            homeSuburb: function (newval, oldval) {
                if (newval.length > 1) {

                    function response(input) {
                        app.$data.availableHomeSuburbs = input.data;
                    }
                    axios.get('suburbs/?partial=' + newval)
                        .then(response)
                        .catch(function error() {
                        });
                }
            },
            workSuburb: function(newval, oldval) {
                if (newval.length > 1) {
                    function response(input) {
                        app.$data.availableWorkSuburbs = input.data;
                    }
                    axios.get('suburbs/?partial=' + newval)
                        .then(response)
                        .catch(function error() {
                        });
                }
            },
            homePostcode: function (newval, oldval) {
                for (i = 0; i < app.$data.availableHomeSuburbs.length; ++i) {
                    element = app.$data.availableSuburbs[i];
                    if (element !== undefined && element.postcode == newval) {
                        console.log(element.suburb)
                        app.$data.selectedSuburb = element.suburb;
                    }
                }
            },
            workPostcode: function(newval, oldval) {
                for (i = 0; i < app.$data.availableWorkSuburbs.length; ++i) {
                    element = app.$data.availableSuburbs[i];
                    if (element !== undefined && element.postcode == newval) {
                        console.log(element.suburb)
                        app.$data.selectedSuburb = element.suburb;
                    }
                }
            }
        },
    });

});
