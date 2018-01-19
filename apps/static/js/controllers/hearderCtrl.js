app.controller("headerCtrl", function($scope, $http, $window, $location) {
    $scope.mama = 123;
    $scope.searchKeyWord = '';
    $http.get('http://localhost:8000/api/categories/?category_type=0')
        .then(
            function (response) {
                $scope.categories = response.data;
            },
            function (response) {
                $scope.categories = [];
            }
        );

    $scope.search = function () {
        $window.location.href = '/product_search/?product_name=' + $scope.searchKeyWord;
    }
});

