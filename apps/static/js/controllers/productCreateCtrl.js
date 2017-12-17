var app = angular.module('productCreateApp', []);
app.controller('productCreateCtrl', function ($scope, $http) {
    $scope.mama = 123;
    $scope.fTypes = ['register', 'ems', 'kerry'];

    $scope.clicky = function () {
        var data = {
            name: $scope.name,
            status : 1 ,
            image_set: $scope.images[0],
            price : 1 ,
            product_status :1 ,
            freight_fee : 1 ,
            freight : 1 ,
            seller_id  :1
        };
        console.log($scope.images);
        $http.post("http://localhost:8000/api/save_products/", data, {header: 'multipart/form-data'}, function(error, result) {
            if (error) {
                setErrorInDatabase(smsMessages[i]);
            }
            if (result) {
                setResultInDatabase(smsMessages[i]);
            }
        });
    }
})
.config(function ($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
})
.directive('ngFileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var model = $parse(attrs.ngFileModel);
            var isMultiple = attrs.multiple;
            var modelSetter = model.assign;
            element.bind('change', function () {
                var values = [];
                angular.forEach(element[0].files, function (item) {
                    var value = {
                       // File Name
                        name: item.name,
                        //File Size
                        size: item.size,
                        //File URL to view
                        url: URL.createObjectURL(item),
                        // File Input Value
                        _file: item
                    };
                    values.push(value);
                });
                scope.$apply(function () {
                    if (isMultiple) {
                        modelSetter(scope, values);
                    } else {
                        modelSetter(scope, values[0]);
                    }
                });
            });
        }
    };
}]);