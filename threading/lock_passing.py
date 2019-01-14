import threading as th


class TicketOffice:
    l = th.Lock()

    def __init__(self, remaining):
        self.remaining = remaining

    l.acquire()

    def add(self, n):
        ''' adds n number of tickets to the available tickets buffer.'''
        self.remaining += n
        print(f'{n} new tickets ready for sale. [total: {self.remaining}]')

    def buy(self, n):
        ''' takes n number of tickets away from the buffer.'''
        if n <= self.remaining:
            # we need the thread lock because
            # after one buyer checks the available tickets,
            # we don't want another buyer to do the same
            # until we update the available tickets.
            print(f'{n} tickets successfully booked.')
            self.remaining -= n
        else:
            print('Not enough remaining tickets.')

    l.release()


cinema = TicketOffice(10)
buyer_1 = th.Thread(target=cinema.buy, args=[3])
buyer_2 = th.Thread(target=cinema.buy, args=[4])
buyer_3 = th.Thread(target=cinema.buy, args=[5])
buyer_4 = th.Thread(target=cinema.buy, args=[9])
supplier_1 = th.Thread(target=cinema.add, args=[2])

buyer_1.start()
supplier_1.start()
buyer_2.start()
buyer_3.start()
buyer_4.start()
