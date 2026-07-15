"use client";

import { useMemo } from "react";
import type { CapabilitiesMap, CapabilityId } from "@/lib/capabilities-registry";
import { hasCap } from "@/lib/capabilities-registry";

interface BranchCapabilitiesResult {
  caps: CapabilitiesMap;
  has: (id: CapabilityId) => boolean;
}

export function useBranchCapabilities(branchSpaceData: { meta?: { capabilities?: CapabilitiesMap } } | null): BranchCapabilitiesResult {
  const caps = useMemo(() => {
    return branchSpaceData?.meta?.capabilities ?? {};
  }, [branchSpaceData]);

  return {
    caps,
    has: (id: CapabilityId) => hasCap(caps, id),
  };
}
