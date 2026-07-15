import { NoteBlocksView } from "@/features/noteblocks";

export const metadata = {
  title: "NoteBlocks",
};

export default async function NoteBlocksPage(props: {
  searchParams?: Promise<{
    noteId?: string;
    session?: string;
    pathId?: string;
  }>;
}) {
  const searchParams = await props.searchParams;
  const noteId = searchParams?.noteId;
  const sessionMode = searchParams?.session === "1";
  const pathId = searchParams?.pathId;

  return (
    <NoteBlocksView
      noteId={noteId}
      sessionMode={sessionMode}
      pathId={pathId}
    />
  );
}
