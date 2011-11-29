import logging
import itertools
import operator
import nose.plugins as np
import sqlalchemy.engine as sa_engine
import sqlalchemy.event as sa_event
from collections import OrderedDict

class CommitReportPlugin(np.Plugin):
    """ report commiting on sqlalchemy engine during testing.
    """

    logger = logging.getLogger("CommitReportPlugin")

    name = "commitreport"

    def begin(self):
        self.commited = OrderedDict()
        self.logger.debug("setting commit report")
        sa_event.listen(sa_engine.Engine, "commit", self.on_commit)

    def on_commit(self, connection):
        if self.current_test:
            self.commited[self.current_test] = self.commited.get(self.current_test, 0) + 1

    def beforeTest(self, test):
        self.current_test = test.address()

    def afterTest(self, test):
        self.current_test = None

    def report(self, out):
        out.write("----------------------------------------------------------------------\n")
        out.write("commit report\n")
        for f, cases in itertools.groupby(self.commit_reports, operator.itemgetter(0)):
            out.write("\n")
            out.write("%s" % f)
            for _, m, t, v in cases:
                out.write("\n")
                out.write("%s.%s commit %d times" % (m, t, v))
            out.write("\n")
        out.write("\n")

    @property
    def commit_reports(self):
        for k, v in self.commited.iteritems():
            yield k[0], k[1], k[2], v
