/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../index";
import * as OpikApi from "../../../../../api/index";
import * as core from "../../../../../core";
import { JsonNode } from "../../../../types/JsonNode";
import { ErrorInfo } from "../../../../types/ErrorInfo";

export const TraceUpdate: core.serialization.Schema<serializers.TraceUpdate.Raw, OpikApi.TraceUpdate> =
    core.serialization.object({
        projectName: core.serialization.property("project_name", core.serialization.string().optional()),
        projectId: core.serialization.property("project_id", core.serialization.string().optional()),
        endTime: core.serialization.property("end_time", core.serialization.date().optional()),
        input: JsonNode.optional(),
        output: JsonNode.optional(),
        metadata: JsonNode.optional(),
        tags: core.serialization.list(core.serialization.string()).optional(),
        errorInfo: core.serialization.property("error_info", ErrorInfo.optional()),
        threadId: core.serialization.property("thread_id", core.serialization.string().optional()),
    });

export declare namespace TraceUpdate {
    export interface Raw {
        project_name?: string | null;
        project_id?: string | null;
        end_time?: string | null;
        input?: JsonNode.Raw | null;
        output?: JsonNode.Raw | null;
        metadata?: JsonNode.Raw | null;
        tags?: string[] | null;
        error_info?: ErrorInfo.Raw | null;
        thread_id?: string | null;
    }
}
