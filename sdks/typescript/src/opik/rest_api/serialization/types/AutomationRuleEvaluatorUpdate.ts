/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../core";
import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import { AutomationRuleEvaluatorUpdateLlmAsJudge } from "./AutomationRuleEvaluatorUpdateLlmAsJudge";
import { AutomationRuleEvaluatorUpdateUserDefinedMetricPython } from "./AutomationRuleEvaluatorUpdateUserDefinedMetricPython";

const _Base = core.serialization.object({
    name: core.serialization.string(),
    samplingRate: core.serialization.property("sampling_rate", core.serialization.number().optional()),
    code: core.serialization.record(core.serialization.string(), core.serialization.unknown()),
    projectId: core.serialization.property("project_id", core.serialization.string().optional()),
    action: core.serialization.stringLiteral("evaluator").optional(),
});
export const AutomationRuleEvaluatorUpdate: core.serialization.Schema<
    serializers.AutomationRuleEvaluatorUpdate.Raw,
    OpikApi.AutomationRuleEvaluatorUpdate
> = core.serialization
    .union("type", {
        llm_as_judge: AutomationRuleEvaluatorUpdateLlmAsJudge.extend(_Base),
        user_defined_metric_python: AutomationRuleEvaluatorUpdateUserDefinedMetricPython.extend(_Base),
    })
    .transform<OpikApi.AutomationRuleEvaluatorUpdate>({
        transform: (value) => value,
        untransform: (value) => value,
    });

export declare namespace AutomationRuleEvaluatorUpdate {
    export type Raw = AutomationRuleEvaluatorUpdate.LlmAsJudge | AutomationRuleEvaluatorUpdate.UserDefinedMetricPython;

    export interface LlmAsJudge extends _Base, AutomationRuleEvaluatorUpdateLlmAsJudge.Raw {
        type: "llm_as_judge";
    }

    export interface UserDefinedMetricPython extends _Base, AutomationRuleEvaluatorUpdateUserDefinedMetricPython.Raw {
        type: "user_defined_metric_python";
    }

    export interface _Base {
        name: string;
        sampling_rate?: number | null;
        code: Record<string, unknown>;
        project_id?: string | null;
        action?: "evaluator" | null;
    }
}
