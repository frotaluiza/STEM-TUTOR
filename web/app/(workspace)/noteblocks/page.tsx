import { NoteBlocksView } from "@/features/noteblocks";

export const metadata = {
  title: "NoteBlocks",
};

export default async function NoteBlocksPage(props: {
  searchParams?: Promise<{ noteId?: string }>;
}) {
  const searchParams = await props.searchParams;
  const noteId = searchParams?.noteId;

  return <NoteBlocksView noteId={noteId} />;
}
