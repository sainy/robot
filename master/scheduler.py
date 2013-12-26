from buildbot.schedulers import base
from buildbot.schedulers.basic import SingleBranchScheduler
from twisted.internet import defer
from buildbot.changes import filter
from twisted.python import log

class SingleBranchSchedulerBase(SingleBranchScheduler):
    counter_cls_num = 0

    def __init__(self, name, max_cls_num = None, **kwargs):
        self.max_cls_num = max_cls_num
        SingleBranchScheduler.__init__(self, name, **kwargs)

    def stableTimerFired(self, timer_name):
        self.counter_cls_num = 0
        return SingleBranchScheduler.stableTimerFired(self,timer_name)

class SingleBranchSchedulerOne(SingleBranchSchedulerBase):

    def __init__(self, **kwargs):
        SingleBranchSchedulerBase.__init__(self, **kwargs)
    
    def gotChange(self, change, important):
        if not self.treeStableTimer:
            if not important:
                return defer.succeed(None)
            return self.addBuildsetForChanges(reason=self.reason, changeids=[change.number])
        else:
            timer_name = self.getTimerNameForChange(change)
        
            d = self.master.db.schedulers.classifyChanges(self.objectid, {change.number: important})

            def fix_timer(_):
                if not important and not self._stable_timers[timer_name]:
                    return
                if self._stable_timers[timer_name]:
                    if self.max_cls_num and self.counter_cls_num < self.max_cls_num-1:
                        self.counter_cls_num += 1
                        self._stable_timers[timer_name].cancel()
                    else:
                        self._stable_timers[timer_name].cancel()
                        df = self.stableTimerFired(timer_name)
                        df.addErrback(log.err, "while firing stable timer")
                        return 
                else:
                    self.counter_cls_num += 1

                def fire_timer():
                    d = self.stableTimerFired(timer_name)
                    d.addErrback(log.err, "while firing stable timer")
                self._stable_timers[timer_name] = self._reactor.callLater(self.treeStableTimer, fire_timer)
            d.addCallback(fix_timer)
            return d


class SingleBranchSchedulerTwo(SingleBranchSchedulerBase):
 
    def __init__(self, name, max_cls_num = None, **kwargs):
        SingleBranchSchedulerBase.__init__(self, name, max_cls_num, **kwargs)

    def gotChange(self, change, important):
        if not self.treeStableTimer:
            if not important:
                return defer.succeed(None)
            return self.addBuildsetForChanges(reason=self.reason, changeids=[change.number])
        else:
            timer_name = self.getTimerNameForChange(change)
        
            d = self.master.db.schedulers.classifyChanges(self.objectid, {change.number: important})

            def fix_timer(_):
                if not important and not self._stable_timers[timer_name]:
                    return
                if self._stable_timers[timer_name]:
                    if self.max_cls_num and self.counter_cls_num < self.max_cls_num - 1:
                        self.counter_cls_num += 1
                        return
                    else:
                        self._stable_timers[timer_name].cancel()
                        df = self.stableTimerFired(timer_name)
                        df.addErrback(log.err, "while firing stable timer")
                        return 
                else:
                    self.counter_cls_num += 1

                def fire_timer():
                    d = self.stableTimerFired(timer_name)
                    d.addErrback(log.err, "while firing stable timer")
                self._stable_timers[timer_name] = self._reactor.callLater(self.treeStableTimer, fire_timer)
            d.addCallback(fix_timer)
            return d

