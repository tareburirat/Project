app.controller("headerCtrl", function($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.searchKeyWord = '';
    $http.get($scope.mama + '/api/categories/?category_type=0')
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

