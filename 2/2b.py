from mrjob.job import MRJob

class PageRank(MRJob):
    def configure_args(self):
        super(PageRank, self).configure_args()
        self.add_passthru_arg('--damping-factor', type=float, default=0.85)
        self.add_passthru_arg('--num-pages', type=int, required=True)

    def mapper(self, _, line):
        # Parse a line of input
        parts = line.split('\t')
        page = parts[0]
        links = parts[1].split(',')

        # Distribute the PageRank equally among linked pages
        rank = float(parts[2]) / len(links)

        # Emit the contribution to each linked page
        for link in links:
            yield link, rank

        # Emit the page itself with its links for the next iteration
        yield page, links

    def reducer(self, page, values):
        new_rank = 0.0
        links = []

        for value in values:
            if isinstance(value, list):
                links = value
            else:
                new_rank += value

        damping_factor = self.options.damping_factor
        num_pages = self.options.num_pages

        # Calculate the new PageRank using the damping factor
        new_rank = (1 - damping_factor) / num_pages + damping_factor * new_rank

        # Emit the updated PageRank for the page
        yield page, new_rank

if __name__ == '__main__':
    PageRank.run()
