app.controller("displayCtrl", function ($scope, $window, $http, $rootScope) {
    var vm = this;
    vm.yoyo = 123;
    var paramString = "";
    vm.categories = [];

    vm.getData = function () {
        var queryString = "http://localhost:8000/dashboard/cat_summary?" + paramString;
        $http.get(queryString).then(
            function success(response) {
                vm.categories = response.data;
            },
            function (response) {
                alert('Failed');
            }
        )
    };
    vm.getData();
});