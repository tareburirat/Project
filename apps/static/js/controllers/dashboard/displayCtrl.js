app.controller("displayCtrl", function ($scope, $window, $http, $rootScope) {
    var hostUrl = $rootScope.url;
    var vm = this;
    vm.yoyo = 123;
    vm.categories = [];
    var now = new Date();
    vm.currentYears = [];
    vm.days = 30;
    vm.searchMode = ['Date', 'Month', 'Year'];
    vm.selectedMode = 'Year';
    vm.tables = ['Products', 'Rating', 'Purchased Products'];
    vm.table = 'Products';
    var graphData = [];
    var graphHeader = [];

    vm.updateYear = function (currentYear) {
        vm.currentYears = [currentYear - 1, currentYear, currentYear + 1];
        if (vm.currentYears % 4 === 0 && vm.currentMonth === 'February') {
            vm.days = 29;
        }
    };
    vm.monthMapper = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    vm.updateMonth = function (currentMonth) {
        if (currentMonth in ['January', 'March', 'May', 'July', 'August', 'October', 'December']) {
            vm.days = 31;
        }
        else if (currentMonth in ['April', 'June', 'September', 'November']) {
            if (currentMonth in ['January', 'March', 'May', 'July', 'August', 'October', 'December']) {
                vm.days = 30
            }
            else if (currentMonth === "February") {
                vm.days = 28;
                if (vm.currentYears % 4 === 0 && vm.currentMonth === 'February') {
                    vm.days = 29;
                }
            }
        }
    };
    vm.updateDay = function (currentDay) {
        vm.currentDays = [currentDay - 1, currentDay, currentDay + 1]
    };
    vm.updateYear(now.getFullYear());
    vm.currentYear = now.getFullYear();
    vm.currentMonth = vm.monthMapper[now.getMonth()];
    vm.updateDay(now.getDate());
    vm.currentDay = now.getDate();


    var getParamString = function () {
        var paramString = "";
        if (vm.selectedMode === 'Year') {
            paramString = 'mode=year&year=' + vm.currentYear;
        }
        else if (vm.selectedMode === 'Month') {
            paramString = 'mode=month&year=' + vm.currentYear;
            paramString = paramString + '&month=' + vm.monthMapper.indexOf(vm.currentMonth);
        }
        else if (vm.selectedMode === 'Date') {
            paramString = 'mode=day&year=' + vm.currentYear;
            paramString = paramString + '&month=' + vm.monthMapper.indexOf(vm.currentMonth);
            paramString = paramString + '&day=' + vm.currentDay;
        }
        return paramString
    };
    vm.search = function (table) {
        if (table === 'Products') {
            var queryString = hostUrl + "/dashboard/cat_summary?" + getParamString();
            $http.get(queryString).then(
                function success(response) {
                    vm.categories = response.data;
                    buildGraph();
                },
                function (response) {
                    alert('Failed');
                }
            )
        }
        else if (table === 'Purchased Products') {
            getPurchasedProduct();
        }
    };

    vm.getData = function () {
        // paramString = 'mode=' +  vm.selectedMode + '&&year=' + vm.currentYears+ '&&day=' + vm.currentDay+ '&&day=' + vm.currentDay;
        var queryString = hostUrl + "/dashboard/cat_summary?";
        $http.get(queryString).then(
            function success(response) {
                vm.categories = response.data;
                buildGraph();
            },
            function (response) {
                alert('Failed');
            }
        )
    };
    vm.getData();

    vm.range = function (min, max, step) {
        step = step || 1;
        var input = [];
        for (var i = min; i <= max; i += step) input.push(i);
        return input;
    };

    vm.updateTable = function (table) {
        if (table === 'Rating') {
            getRating();
        }
        else if (table === 'Purchased Products') {
            getPurchasedProduct();
        }
    };

    var getRating = function () {
        $http.get(hostUrl + '/api/best_ratings_data/').then(
            function (response) {
                vm.shops = response.data;
            }
        )
    };

    var getPurchasedProduct = function () {
        $http.get(hostUrl + '/dashboard/purchased_summary/?' + getParamString()).then(
            function (response) {
                vm.purchasedProductSummary = response.data;
            }
        )
    };

    var buildGraph = function () {
        graphHeader = [];
        graphData = [];
        angular.forEach(vm.categories.slice(0, 5), function (category) {
            graphHeader.push(category.name);
            graphData.push(category.product_count);
        });
        new Chart(document.getElementById("bar-chart"), {
            type: 'bar',
            data: {
                // labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
                labels: graphHeader,
                datasets: [
                    {
                        label: "Population (millions)",
                        backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                        // data: [2478,5267,734,784,433]
                        data: graphData
                    }
                ]
            },
            options: {
                legend: {display: false},
                title: {
                    display: true,
                    text: 'Predicted world population (millions) in 2050'
                }
            }
        });
    }

});