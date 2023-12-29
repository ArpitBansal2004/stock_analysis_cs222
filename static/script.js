function updateStockChart() {
    var selectedValue = document.getElementById('stock-select').value;
    var stockCode = selectedValue === 'other' ? document.getElementById('custom-stock-symbol').value : selectedValue;

    if (!stockCode) {
        alert('Please enter a stock code.');
        return;
    }

    fetch('/predict/' + stockCode)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                alert(data.error);  // Display an alert with the error message
            } else {
                var chartContainer = document.getElementById('chart-container');
                chartContainer.innerHTML = '<img src="' + data.chartPath + '" alt="Stock Chart">';
            }
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            alert('Failed to retrieve stock data. Please check the stock symbol.');
        });
}

function toggleCustomStockInput(value) {
    var customInput = document.getElementById('custom-stock-input');
    if (value === 'other') {
        customInput.style.display = 'block';
    } else {
        customInput.style.display = 'none';
    }
}
