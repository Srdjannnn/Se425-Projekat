document.addEventListener('DOMContentLoaded', function() {
    const seats = document.querySelectorAll('.seat.available');
    const buyBtn = document.getElementById('buy-btn');
    const form = document.getElementById('buy-form');
    const selectedSeatInput = document.getElementById('selected-seat');

    seats.forEach(seat => {
        seat.addEventListener('click', function() {
            // Remove selected from others
            document.querySelectorAll('.seat.selected').forEach(s => s.classList.remove('selected'));
            // Add selected to this
            this.classList.add('selected');
            selectedSeatInput.value = this.dataset.seatId;
            buyBtn.disabled = false;
            // Set form action
            form.action = `/buy/${eventId}/${this.dataset.seatId}`;
        });
    });
});