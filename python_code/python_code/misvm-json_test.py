#--*coding:utf-8 --*
import json
'''high起来'''
def misvm2dict(misvm_example):
    return{
        'restarts':misvm_example.restarts,
        'max_iters':misvm_example.max_iters,
        'C':misvm_example.C,
        '_x':misvm_example._x,
        '_alphas':misvm_example._alphas,
        '_b':misvm_example._b,
        '_bag_predictions':misvm_example._bag_predictions,
        '_bags':misvm_example._bags,
        '_estimator_type':misvm_example._estimator_type,
        '_objective':misvm_example._objective,
        '_predictions':misvm_example._predictions,
        '_sv':misvm_example._sv,
        '_sv_X':misvm_example._sv_X,
        '_sv_alphas':misvm_example._sv_alphas,
        '_sv_y':misvm_example._sv_y,
        '_y':misvm_example._y,
        'gamma':misvm_example.gamma,
        'kernel':misvm_example.kernel,
        'p':misvm_example.p,
        'scale_C':misvm_example.scale_C,
        'sv_cutoff':misvm_example.sv_cutoff,
        'verbose':misvm_example.verbose,
        }
def dict_unpackage(misvm,misvm_example):
        misvm.restarts=misvm_example.restarts
        misvm.max_iters=misvm_example.max_iters
        misvm.C=misvm_example.C
        misvm._x=misvm_example._x
        misvm._alphas=misvm_example._alphas
        misvm._b=misvm_example._b
        misvm._bag_predictions=misvm_example._bag_predictions
        misvm._bags=misvm_example._bags
        misvm._estimator_type=misvm_example._estimator_type
        misvm._objective=misvm_example._objective
        misvm._predictions=misvm_example._predictions
        misvm._sv=misvm_example._sv
        misvm._sv_X=misvm_example._sv_X
        misvm._sv_alphas=misvm_example._sv_alphas
        misvm._sv_y=misvm_example._sv_y
        misvm._y=misvm_example._y
        misvm.gamma=misvm_example.gamma
        misvm.kernel=misvm_example.kernel
        misvm.p=misvm_example.p
        misvm.scale_C=misvm_example.scale_C
        misvm.sv_cutoff=misvm_example.sv_cutoff
        misvm.verbose=misvm_example.verbose
        return  misvm


